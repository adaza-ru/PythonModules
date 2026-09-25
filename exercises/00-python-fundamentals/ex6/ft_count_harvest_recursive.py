#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 19:53:33 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/24 17:52:59 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))

    def count_recursive(day: int) -> None:
        if day > n:
            return
        print(f"Day {day}")
        count_recursive(day + 1)

    count_recursive(1)
    print("Harvest time!")
