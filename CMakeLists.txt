cmake_minimum_required(VERSION 3.6...3.10)
project(monty_hall)

set(PYBIND11_PYTHON_VERSION 3.6.9 CACHE STRING "")

set(CMAKE_CXX_STANDARD 14)

add_subdirectory(pybind11)

add_library(monty_hall_wrapper MODULE cpp/monty_hall_wrapper.cpp cpp/monty_hall.h)
target_link_libraries(monty_hall_wrapper PRIVATE pybind11::module)

set_target_properties(monty_hall_wrapper PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/env)
pybind11_extension(monty_hall_wrapper)
pybind11_strip(monty_hall_wrapper)
