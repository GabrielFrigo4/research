#ifndef SAMPLE_ALGORITHM_HPP
#define SAMPLE_ALGORITHM_HPP

#include "../core/AlgorithmBase.hpp"

class SampleAlgorithm final : public AlgorithmBase
{
public:
	explicit SampleAlgorithm(const Size n) : AlgorithmBase(n) {}

	static std::unique_ptr<AlgorithmBase> create(const Size n)
	{
		return std::make_unique<SampleAlgorithm>(n);
	}

	std::unique_ptr<AlgorithmBase> make(const Size n) const override
	{
		return std::make_unique<SampleAlgorithm>(n);
	}

	std::unique_ptr<AlgorithmBase> clone() const override
	{
		return std::make_unique<SampleAlgorithm>(*this);
	}

	Long solve() override
	{
		Long total = 0;
		for (const Long value : data)
			total += value;
		return total;
	}
};

#endif
