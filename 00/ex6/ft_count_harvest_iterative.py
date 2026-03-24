#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 19:46:18 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/24 17:47:48 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative() -> None:
    n = int(input("Days until harvest: "))
    for day in range(1, n + 1):
        print(f"Day {day}")
    print("Harvest time!")
