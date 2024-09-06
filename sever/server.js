require("dotenv").config();
const express = require("express");
const cors=require("cors");
const app = express();

const authRoute = require("./router/auth-router");  // Enclosed the path in quotes
const contactRoute=require("./router/contact-router")
const connectDb=require("./utils/db");
const errorMiddleware=require("./middlewares/error-middleware");

//let's tackle the cors 
const corsOptions={
    origin:"http://localhost:5173",
    methods:"GET,POST,PUT,DELETE,PATCH,HEAD",
    credentials:true,
};
app.use(cors(corsOptions));
app.use(express.json());
app.use("/api/auth", authRoute);
app.use("/api/form",contactRoute)
app.use(errorMiddleware);
const port = 3000;
connectDb().then(()=>{
    app.listen(port, () => {
    console.log(`server is running at port: ${port}`);
    });
});

