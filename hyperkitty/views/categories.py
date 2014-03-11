#-*- coding: utf-8 -*-
# Copyright (C) 1998-2012 by the Free Software Foundation, Inc.
#
# This file is part of HyperKitty.
#
# HyperKitty is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# HyperKitty is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# HyperKitty.  If not, see <http://www.gnu.org/licenses/>.
#
#


import datetime

from django.shortcuts import render
from django.conf import settings

from hyperkitty.lib import get_store
from hyperkitty.lib.view_helpers import show_mlist
from hyperkitty.lib.mailman import is_mlist_authorized

if settings.USE_MOCKUPS:
    from hyperkitty.lib.mockup import generate_threads_per_category

def categories(request):
    if settings.USE_MOCKUPS:
        categories = generate_threads_per_category()
        #categories = sorted(categories, key=lambda category: category.name)
    else:
        categories = {}

    # sorting
    sort_mode = request.GET.get('sort')
    #if sort_mode == "subscribed":
    #    lists.sort(key=lambda l: l.recent_threads_count, reverse=True)
    #elif sort_mode == "unsubscribed":
    #    lists.sort(key=lambda l: l.recent_participants_count, reverse=True)
    #else:
    #    sort_mode = None

    context = {
        'view_name': 'categories',
        'categories': categories,
        'sort_mode': sort_mode,
        }
    return render(request, "categories.html", context)
