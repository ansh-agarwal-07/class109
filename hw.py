import pandas as pd
import statistics 
import csv

df = pd.read_csv('height-weight.csv')
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()
h_mean = statistics.mean(height_list)
w_mean = statistics.mean(weight_list)

h_median = statistics.median(height_list)
w_median = statistics.median(weight_list)

h_mode = statistics.mode(height_list)
w_mode = statistics.mode(weight_list)

print("mean,median,mode of height is {},{},{} respectively".format(h_mean, h_median, h_mode))
print("mean,median,mode of weight is {},{},{} respectively".format(w_mean, w_median, w_mode))

h_std = statistics.stdev(height_list)
w_std = statistics.stdev(weight_list)
h_first_std_deviation_start,h_first_std_deviation_end = h_mean - h_std, h_mean + h_std
h_second_std_deviation_start,h_second_std_deviation_end =h_mean-(2*h_std),h_mean+(2*h_std)
h_third_std_deviation_start,h_third_std_deviation_end =h_mean-(3*h_std),h_mean+(3*h_std)

w_first_std_deviation_start,w_first_std_deviation_end = w_mean - w_std, w_mean + w_std
w_second_std_deviation_start,w_second_std_deviation_end =w_mean-(2*w_std),w_mean+(2*w_std)
w_third_std_deviation_start,w_third_std_deviation_end =w_mean-(3*w_std),w_mean+(3*w_std)

h_list_of_data_within_1_std_deviation = [result for result in height_list if result > h_first_std_deviation_start and result < h_first_std_deviation_end]
h_list_of_data_within_2_std_deviation = [result for result in height_list if result > h_second_std_deviation_start and result < h_second_std_deviation_end]
h_list_of_data_within_3_std_deviation = [result for result in height_list if result > h_third_std_deviation_start and result < h_third_std_deviation_end]

w_list_of_data_within_1_std_deviation = [result for result in weight_list if result > w_first_std_deviation_start and result < w_first_std_deviation_end]
w_list_of_data_within_2_std_deviation = [result for result in weight_list if result > w_second_std_deviation_start and result < w_second_std_deviation_end]
w_list_of_data_within_3_std_deviation = [result for result in weight_list if result > w_third_std_deviation_start and result < w_third_std_deviation_end]

print("{}%  of data for height lies within 1 standard deviation".format(len(h_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}%  of data for height lies within 2 standard deviation".format(len(h_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}%  of data for height lies within 3 standard deviation".format(len(h_list_of_data_within_3_std_deviation)*100.0/len(height_list)))

print("{}%  of data for weight lies within 1 standard deviation".format(len(w_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}%  of data for weight lies within 2 standard deviation".format(len(w_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}%  of data for weight lies within 3 standard deviation".format(len(w_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))