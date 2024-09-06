const { z } = require("zod");

// User validation schema using Zod in Node.js and Express.js
const signupSchema = z.object({
    username: z
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
    phone: z
        .string({ required_error: "Phone number is required" })
        .trim()
        .length(10, { message: "Phone number must be exactly 10 digits" }),
    password: z
        .string({ required_error: "Password is required" })
        .trim()
        .min(7, { message: "Password must be at least seven letters/characters" })
        .max(1024, { message: "Password should not be more than 1024 letters/characters" }),
});

module.exports = signupSchema;
