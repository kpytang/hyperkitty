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
from operator import attrgetter

from django.shortcuts import render
from django.conf import settings

from hyperkitty.lib import get_store
from hyperkitty.lib.view_helpers import show_mlist
from hyperkitty.lib.mailman import is_mlist_authorized

if settings.USE_MOCKUPS:
    from hyperkitty.lib.mockup import generate_threads_per_category, generate_random_thread

def categories(request):
    categories = {}
    if settings.USE_MOCKUPS:
        categories, threads_by_category = generate_threads_per_category()
        categories = sorted(categories, key=lambda category:category.name)

    context = {
        'view_name': 'categories',
        'categories': categories,
        'category_threads': threads_by_category,
    }
    return render(request, "categories.html", context)

def category(request, category_label):
    category_threads = []
    category_obj = None
    if settings.USE_MOCKUPS:
        categories, threads_by_category = generate_threads_per_category()
        for category in categories:
            if category.name == category_label:
                break
        if category is not None:
            if category.name in threads_by_category:
                category_threads = threads_by_category[category.name]
            category_threads.sort(key=lambda thread:thread.date)

    context = {
        'view_name': 'categories',
        'category': category,
        'category_threads': category_threads,
    }
    return render(request, "category.html", context)
