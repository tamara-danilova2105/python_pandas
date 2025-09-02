from app.features.build_features import (
    load_data, 
    add_is_adult, 
    save_data, 
    get_info_lesson_one, 
    add_salary_in_k, 
    group_by_city, 
    sort_by_age,
    filter_age_30_plus,
    filter_moscow,
    count_people_by_city,
    city_with_max_avg_salary,
    names_to_lower,
    add_has_a,
    add_name_length,
    filter_adults_novosib,
    top_2_by_salary,
    stats_by_city,
) 

def main():
    df = load_data()
    df = add_is_adult(df)
    df = get_info_lesson_one(df)
    df = add_salary_in_k(df)
    df = group_by_city(df)
    df = sort_by_age(df)
    df = filter_age_30_plus(df)
    df = filter_moscow(df)
    df = count_people_by_city(df)
    df = city_with_max_avg_salary(df)
    df = names_to_lower(df)
    df = add_has_a(df)
    df = add_name_length(df)
    df = filter_adults_novosib(df)
    df = top_2_by_salary(df)
    df = stats_by_city(df)
    save_data(df)
    print("✅ Обработка завершена")

if __name__ == "__main__":
    main()
