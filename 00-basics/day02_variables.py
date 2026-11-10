quantity = 6
total_price = chai_price * quantity
print("Naya bill:", total_price, "rupees") #total_price = 60 ban gaya

--------------------------------------
quantity = 6
total_price = chai_price * quantity
print("Naya bill:", total_price, "rupees")

quantity = 4
total_price = chai_price * quantity   # yahan total_price = 60 ban gaya
quantity = 6
print(total_price)                    # phir bhi 60! (Kyun? Line total_price = chai_price * quantity sirf ek baar chalti hai, us waqt jo values thi unse. Usne 15 × 4 = 60 nikala aur dabbe mein rakh diya. Baad mein quantity badalne se total_price apne aap update nahi hota.
Example se: dukaandar ne 4 chai ka bill print kar diya: ₹60. Ab aap bolo “6 chai kar do”. Purana kaagaz apne aap ₹90 nahi ho jayega. Naya bill banana padega.
(Excel use kiya hai to: wahan formula apne aap update hota hai, Python mein nahi.))

---------------------------------
#Sahi tareeka

#new file
chai_price = 15
quantity = 4
total_price = chai_price * quantity
print("Bill:", total_price)       # Bill: 60

quantity = 6
total_price = chai_price * quantity   # naya bill banaya
print("Naya bill:", total_price)  # Naya bill: 90
