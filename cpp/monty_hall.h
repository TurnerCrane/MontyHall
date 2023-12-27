#include <vector>
#include <random>

class MontyHallEnv {
	public:
		MontyHallEnv(int num_doors, int seed) : num_doors_(num_doors), gen_(seed), dis_(0, num_doors - 1) {
			reset();
		}

		int reset() {
			prize_door_ = dis_(gen_);
			chosen_door_ = dis_(gen_);
			return chosen_door_;
		}

		std::pair<int, double> step(int action) {
      if(action == 1) {
        if(chosen_door_ == prize_door_) {
          while(chosen_door_ == prize_door_){
            chosen_door_ = dis_(gen_);
          }
        }else{
                chosen_door_ = prize_door_;
        }
      }
      double reward = (chosen_door_ == prize_door_) ? 1.0 : 0.0;
      return std::make_pair(chosen_door_, reward);
		}

	private:
		int num_doors_;
		int prize_door_;
		int chosen_door_;
		std::mt19937 gen_;
		std::uniform_int_distribution<> dis_;
};
