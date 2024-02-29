import streamlit as st

st.header("Primitive Root🔐")
st.sidebar.write("Primitive Root🔐")

st.write("Welcome to Primitive Root!!")

def is_prime(q):
    if q < 2:
        return False
    for i in range(2, int(q**0.5) + 1):
        if q % i == 0:
            return False
    return True
        
def is_primitive(base, q):
    powers = set()
    result = 1
    
    for i in range(1, q):
        result = (result * base) % q
        powers.add(result)
        st.write(f"{base}^{i} mod {q} = {result}", end=', ' if i < q - 1 else ' ')
        
        if result == 1:
            break
           
    if powers == set(range(1, q)):
        st.write(f"==> {base} is primitive root of {q},")
        return True
    st.write()
    return False
        
def main():
    q = int(st.number_input('Enter a prime number (q):', value=0))
    g = int(st.number_input('Enter a number (g):', value=0))

    if not q or not g:
        st.warning("Please enter valid values for Modulus and Primitive.")
        return
    
    s_button = st.button('Submit', type='primary')
    if s_button:
        if not is_prime(q):
            st.warning(f"{q} is not a prime number!!") 
        else:
            primitive_roots = []
            for base in range(1, q):
                if is_primitive(base, q):
                    primitive_roots.append(base)
                    
            if g in primitive_roots:
                st.write(f"{g} is primitive root: True", primitive_roots)
            else:
                st.write(f"{g} is NOT primitive root of {q} - List of Primitive roots:", primitive_roots)
            
if __name__ == '__main__':
    main()
