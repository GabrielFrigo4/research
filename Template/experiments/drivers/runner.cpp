#include "../../implementations/algorithms/SampleAlgorithm.hpp"
#include <chrono>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char **argv)
{
	if (argc < 2)
	{
		std::cerr << "Usage: runner <instance_file|size>\n";
		return 1;
	}

	const std::string arg = argv[1];
	std::ifstream in(arg);
	Size n = 0;

	std::unique_ptr<AlgorithmBase> solver;
	if (in.is_open())
	{
		if (!(in >> n))
			return 1;
		solver = SampleAlgorithm::create(n);
		for (Size i = 0; i < n; ++i)
		{
			Long v = 0;
			in >> v;
			solver->add_item(i, v);
		}
	}
	else
	{
		n = static_cast<Size>(std::strtoull(arg.c_str(), nullptr, 10));
		solver = SampleAlgorithm::create(n);
		for (Size i = 0; i < n; ++i)
			solver->add_item(i, static_cast<Long>(i + 1));
	}

	const auto t0 = std::chrono::steady_clock::now();
	const Long ans = solver->solve();
	const auto t1 = std::chrono::steady_clock::now();

	const double elapsed_ms = std::chrono::duration<double, std::milli>(t1 - t0)
	                              .count();
	std::cout << "SampleAlgorithm," << n << "," << elapsed_ms << "," << ans << '\n';
	return 0;
}
