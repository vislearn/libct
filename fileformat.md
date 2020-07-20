## Input File Format

The format of the processed input file is a simple text representation of the tracking model.
Empty lines are ignored.
Each line starts with an identifier that specifies how the rest of the line is interpreted.

The model files that have been used for the AISTATS 2020 submission can be found [here][AISTATS2020 Dataset].

### Comments

If a line starts with an `#` the remainder of the line is ignored.

### Segmentation Hypothesis

Format:<br/>
`H $timestep $unique_segmentation_id $cost ($centroid_x, $centroid_y)`

Each segmentation hypothesis belongs to exactly time step (`$timestep`, number greater or equal to zero).
To later refer to one specific segmentation hypothesis the line defines a unique identifier (`$unique_hypothesis_id`, arbitrary string that does not contain spaces).
The unique identifier must be unique across all time steps of the model.
For example, one could use a running counter for all segmentation hypotheses of the model to obtain the unique identifier when writing the model file.
Both centroid location (`$centroid_x` and `$centroid_y`) only serve debugging purposes are otherwise not used.

### Event Definitions

The model contains different events that are attached to one, two or three segmentation candidates.
Examples are cell appearances, cell disappearances and links between two consecutive image frames like movements and divisions.
Each event has a unique event identifier which is again unique across the whole model.
To obtain a suitable value while writing the model file one can use a running counter for all events.
Each event is associated with a cost.

Format for Appearance:<br/>
`APP $unique_event_id $segmentation_id $cost`

Format for Disappearance:<br/>
`DISAPP $unique_event_id $segmentation_id $cost`

Format for Movement:<br/>
`MOVE $unique_event_id $segmentation_id_left $segmentation_id_right $cost`

Format for Movement:<br/>
`DIV $unique_event_id $segmentation_id_left $segmentation_id_right1 $segmentation_id_right2 $cost`


[AISTATS2020 Dataset]: https://hci.iwr.uni-heidelberg.de/vislearn/HTML/people/stefan_haller/datasets/aistats2020_cell_tracking.tar.xz
