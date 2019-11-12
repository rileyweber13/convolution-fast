# Fast image convolution in C++
Includes handwritten CPU implementation using OpenMP, handwritten GPU
implementation using CUDA, and implementations using some tools (like
arrayFire)

# Running
first, make sure you have conan installed (`pip install conan`)

    mkdir build
    cd build
    conan install ..
    cd ..
    make