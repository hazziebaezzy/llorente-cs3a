import streamlit as st

st.balloons()
st.header("Primitive Root🔐🔐")
st.sidebar.write("Primitive Root🔐")

st.write("Welcome to Primitive Root!!")

q = int(input())
g = int(input())

values = []
final_values = []
primitive_frequency = {}
flag = True

def is_prime(num):
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

s_button = st.button('Submit', type='primary')
if s_button:
    if is_prime(q):
        for i in range(1, q):
            for j in range(1, q):
                num1 = ((i ** j) % q)
                if num1 not in primitive_frequency:
                    st.write(f"{i}^{j} mod {q} = {num1}", end="")
                    primitive_frequency[num1] = True
                    values.append(num1)
                else:
                    flag = False
                    break
                if j != q - 1:
                    st.write(",", end="")
                    st.write(" ", end="")
            if len(values) == q - 1:
                st.write(f" ==> {i} is primitive root of {q},", end="")
            st.write()
            if len(values) == len(list(set(values))) and flag:
                final_values.append(i)
            primitive_frequency = {}
            values = []
            flag = True
        if is_prime(g):
            st.write(f"{g} is primitive root: {is_prime(g)} {final_values}")
        else:
            st.write(f"{g} is NOT primitive root of 11 - List of Primitive roots: {final_values}")
    else:
        st.write(f"{q} is not a prime number!!")
