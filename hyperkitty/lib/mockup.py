# -*- coding: utf-8 -*-
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
# Author: Aamir Khan <syst3m.w0rm@gmail.com>
#

import datetime

class Email(object):
    """ Email class containing the information needed to store and
    display email threads.
    """

    def __init__(self):
        """ Constructor.
        Instanciate the default attributes of the object.
        """
        self.email_id = ''
        self.title = ''
        self.body = ''
        self.tags = []
        self.category = None
        self.participants = set(['Pierre-Yves Chibon'])
        self.answers = []
        self.liked = 0
        self.author = ''
        self.avatar = None
        self.list = None

class Author(object):
    """ Author class containing the information needed to get the top
    author of the month!
    """

    def __init__(self):
        """ Constructor.
        Instanciate the default attributes of the object.
        """
        self.name = None
        self.kudos = 0
        self.avatar = None

class Category(object):
    """ Category class containing the information related to categories"""

    def __init__(self):
        """ Constructor.
        Instanciate the default attributes of the object.
        """
        self.name = ''
        self.description = ''
        self.color = None
        self.subscribed = False

class List(object):
    """ Category class containing the information related to categories"""

    def __init__(self):
        """ Constructor.
        Instanciate the default attributes of the object.
        """
        self.name = ''
        self.description = ''
        self.subscribed = False

def get_email_tag(tag):
    threads = generate_random_thread()
    output = []
    for email in threads:
        if tag in email.tags or tag in email.category:
            output.append(email)
        elif email.category_tag and tag in email.category_tag:
            output.append(email)
    return output

def generate_threads_per_category():
    threads = generate_random_thread()
    categories = []
    category_threads = {}
    for thread in threads:
        category = thread.category
        if category is not None:
            categories.append(category)
            if category in category_threads.keys():
                category_threads[category.name].append(thread)
            else:
                category_threads[category.name] = [thread]
    return categories, category_threads

def generate_top_author():
    authors = []

    author = Author()
    author.name = 'Pierre-Yves Chibon'
    author.avatar = 'https://secure.gravatar.com/avatar/072b4416fbfad867a44bc7a5be5eddb9'
    author.kudos = 3
    authors.append(author)

    author = Author()
    author.name = 'Stanislav Ochotnický'
    author.avatar = 'http://sochotni.fedorapeople.org/sochotni.jpg'
    author.kudos = 4
    authors.append(author)

    author = Author()
    author.name = 'Toshio Kuratomi'
    author.avatar = 'https://secure.gravatar.com/avatar/7a9c1d88f484c9806bceca0d6d91e948'
    author.kudos = 5
    authors.append(author)

    return authors

def generate_random_thread():
    threads = []
    
    ## lists for threads
    cloud = List()
    cloud.name = 'cloud'
    cloud.list_address = 'cloud@lists.fedoraproject.org'
    cloud.subscribed = True

    packaging = List()
    packaging.name = 'packaging'
    packaging.list_address = 'packaging@lists.fedoraproject.org'
    packaging.subscribed = False

    ## categories for threads
    todo_category = Category()
    todo_category.name = 'todo'
    todo_category.description = "list of tasks to be completed"
    todo_category.color = '09f'

    agenda_category = Category()
    agenda_category.name = 'agenda'
    agenda_category.description = "agenda items"
    agenda_category.color = 'fa0'
    agenda_category.subscribed = True

    dead_category = Category()
    dead_category.name = 'dead'
    dead_category.description = "inactive discussions"
    dead_category.color = None

    ## 1
    email = Email()
    email.email_id = 1
    email.title = 'Headsup! krb5 ccache defaults are changing in Rawhide'
    email.age = '7 days'
    email.date = datetime.date.today() - datetime.timedelta(days=7)
    email.body = '''Dear fellow developers,
with the upcoming Fedora 18 release (currently Rawhide) we are going to change the place where krb5 credential cache files are saved by default.

The new default for credential caches will be the /run/user/username directory.
'''
    email.category = todo_category
    email.tags.extend(['rawhide', 'krb5'])
    email.participants = set(['Stephen Gallagher', 'Toshio Kuratomi', 'Kevin Fenzi', 'Seth Vidal'])
    email.answers.extend([1,2,3,4,5,6,7,8,9,10,11,12])
    email.liked = 1
    email.author = 'Stephen Gallagher'
    email.avatar = 'http://fedorapeople.org/~sgallagh/karrde712.png'
    email.list = packaging
    threads.append(email)

    ## 2
    email = Email()
    email.email_id = 2
    email.title = 'Problem in packaging kicad'
    email.age = '6 days'
    email.date = datetime.date.today() - datetime.timedelta(days=6)
    email.body = '''Paragraph 1: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '''
    email.tags.extend(['packaging', 'kicad'])
    email.participants = set(['Pierre-Yves Chibon', 'Tom "spot" Callaway', 'Toshio Kuratomi', 'Kevin Fenzi'])
    email.answers.extend([1,2,3,4,5,6,7,8,9,10,11,12])
    email.liked = 0
    email.author = 'Pierre-Yves Chibon'
    email.avatar = 'https://secure.gravatar.com/avatar/072b4416fbfad867a44bc7a5be5eddb9'
    email.list = cloud
    threads.append(email)

    ## 3
    email = Email()
    email.email_id = 3
    email.title = 'Update Java Guideline'
    email.age = '10 days'
    email.date = datetime.date.today() - datetime.timedelta(days=10)
    email.body = '''Paragraph 1: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '''
    email.tags.extend(['rawhide', 'krb5'])
    email.participants = set(['Stanislav Ochotnický', 'Tom "spot" Callaway', 'Stephen Gallagher', 'Jason Tibbitts', 'Rex Dieter', 'Toshio Kuratomi'])
    email.answers.extend([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
    email.liked = 5
    email.category = todo_category
    email.author = 'Stanislav Ochotnický'
    email.avatar = 'http://sochotni.fedorapeople.org/sochotni.jpg'
    email.list = cloud
    threads.append(email)

    ## 4
    email = Email()
    email.email_id = 4
    email.title = 'Agenda for the next Board Meeting'
    email.age = '1 month'
    email.date = datetime.date.today() - datetime.timedelta(days=30)
    email.body = '''Paragraph 1: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '''
    email.tags.extend(['agenda', 'board'])
    email.participants = set(['Toshio Kuratomi', 'Tom "spot" Callaway', 'Robyn Bergeron', 'Max Spevack'])
    email.answers.extend([1,2,3,4,5,6,7,8,9,10,11,12])
    email.liked = 20
    email.category = agenda_category
    email.author = 'Toshio Kuratomi'
    email.avatar = 'https://secure.gravatar.com/avatar/7a9c1d88f484c9806bceca0d6d91e948'
    email.list = cloud
    threads.append(email)

    ## 5
    email = Email()
    email.email_id = 5
    email.title = 'I told you so! '
    email.age = '2 days'
    email.date = datetime.date.today() - datetime.timedelta(days=2)
    email.body = '''Paragraph 1: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '''
    email.tags.extend(['systemd', 'mp3', 'pulseaudio'])
    email.participants = set(['Pierre-Yves Chibon'])
    email.answers.extend([1,2,3,4,5,6,7,8,9,10,11,12])
    email.liked = 0
    email.author = 'Pierre-Yves Chibon'
    email.avatar = 'https://secure.gravatar.com/avatar/072b4416fbfad867a44bc7a5be5eddb9'
    email.category = dead_category
    email.list = cloud
    threads.append(email)

    return threads
