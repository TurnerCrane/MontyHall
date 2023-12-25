#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "monty_hall.h"

namespace py = pybind11;

PYBIND11_MODULE(monty_hall_wrapper, m) {
	py::class_<MontyHallEnv>(m, "MontyHallEnv")
			.def(py::init<int, int>())
			.def("reset", &MontyHallEnv::reset)
			.def("step", &MontyHallEnv::step);
}
