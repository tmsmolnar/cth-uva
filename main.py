"""
Coding the Humanities course @ Universiteit van Amsterdam - by Tamás Molnár

To run the program, type "python main.py". After that, the program will ask for more input from the user, and presents the choices.
The program visualizes the chosen datasets, and prints the basic statistical information to the command line.
"""

import os, sys
import pandas as pd
from bokeh.io import show
from functions import load_data, merge_dataFrames_index, merge_dataFrames_column, clean_index, clean_index_year, clean_regions, clean_column, clean_age, two_to_one_regions, two_to_one_years, two_to_one_regions_gradszakma ,cds_from_regions, cds_from_age, plot_by_regions, plot_by_age


if __name__ == "__main__":

    try:

        print('Starting the program...')
        if len(sys.argv) == 1:

            print('Current available datasets: | school type | in school | graduated |')
            input_1 = str(input('Welcome! Please specify which dataset would you like to load and analyze: '))            
            input_1 = input_1.lower()
            
            if input_1 == "":
                print('You did not specify any dataset.')
                raise KeyboardInterrupt

            elif input_1 == 'school type':
                print('Level of educations: | elementary school | high school | special school | technical school | vocational school |')
                input_2 = str(input('Please specify the level of education you are interested in: '))
                input_2 = input_2.lower()

                if input_2 == 'elementary school':
                    data = two_to_one_regions('datasets/2005-2015_student_schooltype_region.xls',
                                      'datasets/2016-2019_student_schooltype_region.xls',
                                      0)
                    print(data.describe())
                    p = plot_by_regions(data)
                    show(p)



                elif input_2 == 'high school':
                    data = two_to_one_regions('datasets/2005-2015_student_schooltype_region.xls',
                                      'datasets/2016-2019_student_schooltype_region.xls', 4)
                    print(data.describe())
                    p = plot_by_regions(data)
                    show(p)

                    
                elif input_2 == 'special school':
                    data = two_to_one_regions(
                        'datasets/2005-2015_student_schooltype_region.xls', 'datasets/2016-2019_student_schooltype_region.xls',1)
                    print(data.describe())
                    p = plot_by_regions(data)
                    show(p)
                    
                elif input_2 == 'technical school':
                    data = two_to_one_regions(
                        'datasets/2005-2015_student_schooltype_region.xls', 'datasets/2016-2019_student_schooltype_region.xls', 2)
                    print(data.describe())
                    p = plot_by_regions(data)
                    show(p)
                    
                elif input_2 == 'vocational school':
                    data = two_to_one_regions(
                        'datasets/2005-2015_student_schooltype_region.xls','datasets/2016-2019_student_schooltype_region.xls', 3)
                    print(data.describe())
                    p = plot_by_regions(data)
                    show(p)
                    
            elif input_1 == 'in school':
                print('Level of educations: | elementary school | high school | special school | technical school | vocational school |')
                input_2 = str(input('Please specify the level of education you are interested in: '))
                input_2 = input_2.lower()

                if input_2 == 'elementary school':
                    data = two_to_one_years(
                        'datasets/2014-2015_student_inschool_age.xls','datasets/2016-2019_student_inschool_age.xls', 0)
                    print(data.describe())
                    p = plot_by_age(data)
                    show(p)

                elif input_2 == 'high school':
                    data = two_to_one_years(
                        'datasets/2014-2015_student_inschool_age.xls', 'datasets/2016-2019_student_inschool_age.xls', 4)
                    print(data.describe())
                    p = plot_by_age(data)
                    show(p)

                elif input_2 == 'special school':
                    data = two_to_one_years(
                        'datasets/2014-2015_student_inschool_age.xls', 'datasets/2016-2019_student_inschool_age.xls', 1)
                    print(data.describe())
                    p = plot_by_age(data)
                    show(p)

                elif input_2 == 'technical school':
                    data = two_to_one_years(
                        'datasets/2014-2015_student_inschool_age.xls', 'datasets/2016-2019_student_inschool_age.xls', 2)
                    print(data.describe())
                    p = plot_by_age(data)
                    show(p)

                elif input_2 == 'vocational school':
                    data = two_to_one_years(
                        'datasets/2014-2015_student_inschool_age.xls', 'datasets/2016-2019_student_inschool_age.xls', 3)
                    print(data.describe())
                    p = plot_by_age(data)
                    show(p)


            elif input_1 == 'graduated':
                print("Graduated from, received 'diploma' from: | elementary school | high school | vocational school |")
                input_2 = str(input('Please specify the level of education you are interested in: '))
                input_2 = input_2.lower()

                if input_2 == 'elementary school':
                    data = two_to_one_regions(
                        'datasets/2005-2015_student_graduated_region.xls', 'datasets/2016-2019_student_graduated_region.xls', 0)
                    print(data.describe())
                    p = plot_by_regions(data)
                    show(p)

                elif input_2 == 'high school':
                    data = two_to_one_regions(
                        'datasets/2005-2015_student_graduated_region.xls', 'datasets/2016-2019_student_graduated_region.xls', 2)
                    print(data.describe())
                    p = plot_by_regions(data)
                    show(p)


                elif input_2 == 'vocational school':
                    data = two_to_one_regions_gradszakma(
                        'datasets/2005-2015_student_graduated_region.xls', 'datasets/2016-2019_student_graduated_region.xls')
                    print(data.describe())
                    p = plot_by_regions(data)
                    show(p)
                    
                             

    except KeyboardInterrupt:
        print('Thank you for trying out my project!')
        print('Quitting the program...')
        sys.exit()
