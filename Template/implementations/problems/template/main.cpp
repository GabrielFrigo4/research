#include "../../algorithms/SampleAlgorithm.hpp"
#include <iostream>

using Solver = SampleAlgorithm;

void task()
{
	Size n;
	if (!(std::cin >> n))
		return;

	const auto solver = Solver::create(n);
	for (Size i = 0; i < n; ++i)
	{
		Long x;
		std::cin >> x;
		solver->add_item(i, x);
	}

	std::cout << solver->solve() << '\n';
}

int main(void)
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);

	task();
	return 0;
}
