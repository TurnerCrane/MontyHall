#include <vector>
#include <random>

class MontyHallEnv {
	public:
		MontyHallEnv(int num_doors, int seed) : num_doors_(num_doors), gen_(seed), dis_(0, num_doors - 1) {
			reset();
		}

		std::vector<double> reset() {
			prize_door_ = dis_(gen_);
			chosen_door_ = -1;
			return std::vector<double>(num_doors_, 0.0);
		}

		std::pair<std::vector<double>, double> step(int action) {
			if(chosen_door_ == -1) {
				chosen_door_ = action;
				return std::make_pair(std::vector<double>(num_doors_, 0.0), 0.0);
			} else {
				if(action == 1) {
					int old_door = chosen_door_;
					while (chosen_door_ == old_door || chosen_door_ == prize_door_) {
						chosen_door_ == dis_(gen_);
					}
				}
				double reward = (chosen_door_ == prize_door_) ? 1.0 : 0.0;
				return std::make_pair(std::vector<double>(num_doors_, 0.0), reward);
			}
		}

	private:
		int num_doors_;
		int prize_door_;
		int chosen_door_;
		std::mt19937 gen_;
		std::uniform_int_distribution<> dis_;
};
