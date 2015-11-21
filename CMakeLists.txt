cmake_minimum_required(VERSION 3.3)
project(Graphic_language_interpreter)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(Graphic_language_interpreter ${SOURCE_FILES})