#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_summary.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 19:58:33 by adaza-ru            #+#    #+#            #
#   Updated: 2026/02/16 19:59:36 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_garden_summary():
    garden_name = input("Enter garden name: ")
    num_plants = input("Enter number of plants: ")
    print(f"Garden: {garden_name}")
    print(f"Plants: {num_plants}")
    print("Status: Growing well!")
