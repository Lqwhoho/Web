#coding=utf-8
from selenium import webdriver

'''
本文件简易的封装定位单位元素和定位一组元素的方法
'''

'''定位单个元素封装'''
def findId(driver,id):
    f = driver.find_element_by_id(id)
    return f

def findName(driver,name):
    f = driver.find_element_by_name(name)
    return f

def findClassName(driver,name):
    f = driver.find_element_by_class_name(name)
    return f

def findAcId(driver,text):
    f = driver.find_element_by_accessibility_id(text)
    return f

def findTagName(driver,name):
    f = driver.find_element_by_tag_name(name)
    return f

def findLinkText(driver,text):
    f = driver.find_element_by_link_text(text)
    return f

def findPLinkText(driver,text):
    f = driver.find_element_by_partial_link_text(text)
    return f

def findXpath(driver,xpath):
    f = driver.find_element_by_xpath(xpath)
    return f

def findCss(driver,css):
    f = driver.find_element_by_css_selector(css)
    return f

'''定义一组元素封装'''
def findsId(driver,id):
    f = driver.find_elements_by_id(id)
    return f

def findsName(driver,name):
    f = driver.find_elements_by_name(name)
    return f

def findsClassName(driver,name):
    f = driver.find_elements_by_class_name(name)
    return f

def findsTagName(driver,name):
    f = driver.find_elements_by_tag_name(name)
    return f

def findsLinkText(driver,text):
    f = driver.find_elements_by_link_text(text)
    return f

def findsPLinkText(driver,text):
    f = driver.find_elements_by_partial_link_text(text)
    return f

def findsXpath(driver,xpath):
    f = driver.find_elements_by_xpath(xpath)
    return f

def findsCss(driver,css):
    f = driver.find_elements_by_css_selector(css)
    return f