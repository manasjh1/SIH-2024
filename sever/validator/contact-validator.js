const { z } = require("zod");
const contactSchema=z.object({
    username:z
        .string({ required_error: "Name is required" })
        .trim()
        .min(3, { message: "Name must be at least three letters/characters" })
        .max(235, { message: "Name should not be more than 235 letters/characters" }),
    email: z
        .string({ required_error: "Email is required" })
        .trim()
        .email({ message: "Email is invalid" })
        .min(10, { message: "Email must be at least ten letters/characters" })
        .max(200, { message: "Email should not be more than 200 letters/characters" }),
    message:z
        .string({required_error:"Name is required"})
        .min(10,{message:"Your message should atleast of 10 letters"})
        .max(1235,{message:"Your message should not exceeds the length of charcaters which 1235 words"}),
});
module.exports=contactSchema;