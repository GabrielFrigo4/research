#include "../algorithms/SampleAlgorithm.hpp"
#include <cassert>
#include <iostream>

int main()
{
	auto solver = SampleAlgorithm::create(4);
	solver->add_item(0, 10);
	solver->add_item(1, 20);
	solver->add_item(2, 12);

	assert(solver->get_size() == 4);
	assert(solver->solve() == 42);

	auto copy = solver->clone();
	assert(copy->solve() == 42);

	std::cout << "All smoke tests passed.\n";
	return 0;
}
