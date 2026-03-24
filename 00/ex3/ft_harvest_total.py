#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 18:17:07 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/24 17:47:36 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total() -> None:
    harvest: list[int] = [0, 0, 0]
    total_harvest: int = 0

    for i in range(3):
        harvest[i] = int(input(f"Day {i + 1} harvest: "))
    for i in range(3):
        total_harvest += harvest[i]
    print(f"Total harvest: {total_harvest}")
