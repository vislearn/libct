project('libct', ['c', 'cpp'], version: '0.1.0', default_options: ['cpp_std=c++17'])

pymod = import('python')
python3 = pymod.find_installation('python3')
gurobi = dependency('gurobi_c++', fallback: ['gurobi-finder', 'gurobi'])
swig = find_program('swig', required: true)

swig_include_dir = meson.source_root() / 'include'
include_dir = include_directories('include')

libct_static = static_library(
  'ct', 'lib/ct.cpp',
  include_directories: include_dir,
  dependencies: [gurobi])

libct_shared = shared_library(
  'ct', 'lib/ct.cpp',
  include_directories: include_dir,
  version: meson.project_version(),
  soversion: '0',
  dependencies: [gurobi])

libct_py = custom_target('libct_py',
  input: ['swig/ct.i', 'include/ct.h'],
  output: ['libct_py.c'],
  command: [swig, '-python', '-noproxy', '-I@0@'.format(swig_include_dir), '-o', '@OUTPUT@', '@INPUT0@'])

python3.extension_module('libct',
  sources: [libct_py],
  include_directories: include_dir,
  link_with: [libct_static],
  dependencies: [python3.dependency()],
  install: true,
  install_dir: python3.get_install_dir(pure: false, subdir: 'ct'))

python3.install_sources([
    'python/ct/__init__.py',
    'python/ct/gurobi.py',
    'python/ct/model.py',
    'python/ct/primals.py',
    'python/ct/rounding.py',
    'python/ct/tracker.py',
    'python/ct/txt.py',
    'python/ct/utils.py'
  ], pure: true, subdir: 'ct')

install_data(['bin/ct'],
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x')

install_headers('include/ct.h')

# vim: set ts=8 sts=2 sw=2 et:
