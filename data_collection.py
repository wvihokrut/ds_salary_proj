#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:13:15 2020

@author: wasurutvihokrut
"""
import glassdoor_scraper as gs
import pandas as pd

path = "/Users/wasurutvihokrut/Desktop/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 20, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)