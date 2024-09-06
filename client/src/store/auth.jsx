import { useContext, useEffect } from "react";
import {createContext} from "react";
import {useState} from "react";
export const AuthContext=createContext();
export const  AuthProvider=({children})=>{
    const [token,setToken]=useState(localStorage.getItem("token"));
    const [user,setUser]=useState("");
    const storeTokenInLS=(serverToken)=> {
        return localStorage.setItem("token",serverToken);
    };
    let isLoggedIn=!!token;
    console.log("isLoggedIN",isLoggedIn);
    //trackling the logout functions
    const LogoutUser=()=>{
        setToken("");
            return localStorage.removeItem("token");
       
    };

    
    //JWTAUTHENTICATION-to get the currently loggedIN user data
    const userAuthentication=async()=>{
       
       try {
        const response=await fetch("http://localhost:3000/api/auth/user",{
            method:"GET",
            headers:{
                Authorization:`Bearer ${token}`,
            }
        });
        if(response.ok){
            const data=await response.json();
            console.log("user data",data.userData);
            setUser(data.userData);
        }
       } catch (error) {
        
       }
        
    }

    useEffect(()=>{
        userAuthentication();
    })

    return(
        <AuthContext.Provider value={{isLoggedIn,storeTokenInLS,LogoutUser,user}}
        >
            {children}
        </AuthContext.Provider>
    );
};
export const useAuth=()=>{
    const authContextValue=useContext(AuthContext);
    if(!authContextValue){
        throw new Error("useAuth used outside of the provider");
    }
    return  authContextValue;
}