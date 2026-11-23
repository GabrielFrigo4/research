#ifndef ALGORITHM_BASE_HPP
#define ALGORITHM_BASE_HPP

#include <cstddef>
#include <limits>
#include <memory>
#include <vector>

using Long = long long;
using Size = std::size_t;

constexpr Long INF = std::numeric_limits<Long>::max() >> 8;
constexpr Size MAX = std::numeric_limits<Size>::max() >> 8;

class AlgorithmBase
{
public:
	explicit AlgorithmBase(const Size n) : size(n), data(n, 0) {}
	virtual ~AlgorithmBase() = default;

	virtual std::unique_ptr<AlgorithmBase> make(const Size n) const = 0;
	virtual std::unique_ptr<AlgorithmBase> clone() const = 0;

	virtual void add_item(const Size index, const Long value)
	{
		if (index < size)
			data[index] += value;
	}

	virtual Long solve() = 0;

	[[nodiscard]] Size get_size() const
	{
		return size;
	}

	[[nodiscard]] const std::vector<Long> &get_data() const
	{
		return data;
	}

protected:
	Size size;
	std::vector<Long> data;
};

#endif
