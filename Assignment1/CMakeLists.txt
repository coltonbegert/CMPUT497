cmake_minimum_required(VERSION 3.5)
project(Assignment1)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    sim.h
    simulator.c)

add_executable(Assignment1 ${SOURCE_FILES})