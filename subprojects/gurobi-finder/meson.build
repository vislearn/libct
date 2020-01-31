project('gurobi-finder', ['cpp'])
compiler = meson.get_compiler('cpp')

helper = find_program('find-gurobi')
output = run_command(helper).stdout().split('\n')

str_inc_dir = output[0]
str_lib_dir = output[1]
str_clib_name = output[2]
str_cpplib_name = output[3]

gurobi = declare_dependency(
  include_directories: str_inc_dir,
  dependencies: [
    compiler.find_library(str_clib_name, dirs: str_lib_dir),
    compiler.find_library(str_cpplib_name, dirs: str_lib_dir)])
