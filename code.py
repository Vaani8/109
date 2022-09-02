import pandas as pd
import statistics as st
import csv

df=pd.read_csv("data.csv")
test_preparation_list=df["test_preparation"].to_list()
parental_level_of_education_list=df["parental_level_of_education"].to_list()

test_preparation_mean=st.mean(test_preparation_list)
parental_level_of_education_mean=st.mean(parental_level_of_education_list)
test_preparation_median=st.median(test_preparation_list)
parental_level_of_education_median=st.median(parental_level_of_education_list)
test_preparation_mode=st.mode(test_preparation_list)
parental_level_of_education_mode=st.mode(parental_level_of_education_list)
test_preparation_sd=st.stdev(test_preparation_list)
parental_level_of_education_sd=st.stdev(parental_level_of_education_list)

print(test_preparation_mean,test_preparation_median,test_preparation_mode)
print(parental_level_of_education_mean,parental_level_of_education_median,parental_level_of_education_mode)

test_preparation_first_std_start,test_preparation_first_std_end=test_preparation_mean-test_preparation_sd,test_preparation_mean+test_preparation_sd
test_preparation_second_std_start,test_preparation_second_std_end=test_preparation_mean-(2*test_preparation_sd),test_preparation_mean+(2*test_preparation_sd)
test_preparation_third_std_start,test_preparation_third_std_end=test_preparation_mean-(3*test_preparation_sd),test_preparation_mean+(3*test_preparation_sd)

parental_level_of_education_first_std_start,parental_level_of_education_first_std_end=parental_level_of_education_mean-parental_level_of_education_sd,parental_level_of_education_mean+parental_level_of_education_sd
parental_level_of_education_second_std_start,parental_level_of_education_second_std_end=parental_level_of_education_mean-(2*parental_level_of_education_sd),parental_level_of_education_mean+(2*parental_level_of_education_sd)
parental_level_of_education_third_std_start,parental_level_of_education_third_std_end=parental_level_of_education_mean-(3*parental_level_of_education_sd),parental_level_of_education_mean+(3*parental_level_of_education_sd)

test_preparation_list_of_data_within_1_std=[result for result in test_preparation_list if result > test_preparation_first_std_start and
                                  result < test_preparation_first_std_end]
test_preparation_list_of_data_within_2_std=[result for result in test_preparation_list if result > test_preparation_second_std_start and
                                  result < test_preparation_second_std_end]
test_preparation_list_of_data_within_3_std=[result for result in test_preparation_list if result > test_preparation_third_std_start and
                                  result < test_preparation_third_std_end]

parental_level_of_education_list_of_data_within_1_std=[result for result in parental_level_of_education_list if result > parental_level_of_education_first_std_start and
                                  result < parental_level_of_education_first_std_end]
parental_level_of_education_list_of_data_within_2_std=[result for result in parental_level_of_education_list if result > parental_level_of_education_second_std_start and
                                  result < parental_level_of_education_second_std_end]
parental_level_of_education_list_of_data_within_3_std=[result for result in parental_level_of_education_list if result > parental_level_of_education_third_std_start and
                                  result < parental_level_of_education_third_std_end]

print("{}% of data for height lies within 1 standard deviation".format(len(test_preparation_list_of_data_within_1_std)*100.0/len(test_preparation_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(test_preparation_list_of_data_within_2_std)*100.0/len(test_preparation_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(test_preparation_list_of_data_within_3_std)*100.0/len(test_preparation_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(parental_level_of_education_list_of_data_within_1_std)*100.0/len(parental_level_of_education_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(parental_level_of_education_list_of_data_within_2_std)*100.0/len(parental_level_of_education_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(parental_level_of_education_list_of_data_within_3_std)*100.0/len(parental_level_of_education_list)))