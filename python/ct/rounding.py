import copy
import itertools

from . import libct as lib
from .gurobi import Gurobi


def extract_primals_from_tracker(model, tracker):
    g = lib.tracker_get_graph(tracker.tracker)
    primals = Primals(model)
    for timestep in range(model.no_timesteps()):
        for detection in range(model.no_detections(timestep)):
            factor = lib.graph_get_detection(g, timestep, detection)
            incoming_primal = lib.detection_get_incoming_primal(factor)
            outgoing_primal = lib.detection_get_outgoing_primal(factor)

            assert (incoming_primal == -1) == (outgoing_primal == -1)
            primals.detection(timestep, detection, (incoming_primal != -1) and (outgoing_primal != -1))

            if incoming_primal >= 0 and incoming_primal < model.no_incoming_edges(timestep, detection):
                primals.incoming(timestep, detection, incoming_primal)

            if outgoing_primal >= 0 and outgoing_primal < model.no_outgoing_edges(timestep, detection):
                primals.outgoing(timestep, detection, outgoing_primal)

    return primals


def extract_primals_from_gurobi(gurobi):
    model = gurobi._model
    primals = Primals(model)
    for timestep in range(model.no_timesteps()):
        for detection in range(model.no_detections(timestep)):
            variables = gurobi._detections[timestep, detection]

            primals.detection(timestep, detection, variables.detection.X > .5)

            for i in range(model.no_incoming_edges(timestep, detection)):
                if variables.incoming[i].X > .5:
                    primals.incoming(timestep, detection, i)

            for i in range(model.no_outgoing_edges(timestep, detection)):
                if variables.outgoing[i].X > .5:
                    primals.outgoing(timestep, detection, i)

    return primals
