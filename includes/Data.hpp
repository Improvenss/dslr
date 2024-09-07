#ifndef DATA_HPP
# define DATA_HPP

# include <string>
# include <sys/time.h>

/**
 * @brief Islem suresini hesaplamak icin kullandigimiz fonksiyon.
 * 
 * Current time --> ct
 * second: 1659960007[000]
 * micro second: [255]371
 * last time --> 1659960007255%
 * 
 * @fn gettimeofday() : Zamani milisecond cinsinden aliyoruz.
 */
// uint64_t	get_current_time(t_base *base)
// {
// 	struct timeval	ct;
// 	uint64_t		past_time;

// 	gettimeofday(&ct, NULL);
// 	past_time = (ct.tv_sec * (uint64_t)1000)
// 		+ (ct.tv_usec / 1000) - base->start_time;
// 	return (past_time);
// }

class Data
{
	private:
	private:
		int				_index;
		std::string		_hogwarts_house;
		std::string		_first_name;
		std::string		_last_name;
		struct timeval	_birthday;
		bool			_best_hand; // If true = left, false = right.
		float			_arithmancy;
		float			_astronomy;
		float			_herbology;
		float			_defense_against_the_dark_arts;
		float			_divination;
		float			_muggle_studies;
		float			_ancient_runes;
		float			_history_of_magic;
		float			_transfiguration;
		float			_potions;
		float			_care_of_magical_creatures;
		float			_charms;
		float			_flying;
	public:
		Data();
		~Data();
};

#endif	//DATA_HPP