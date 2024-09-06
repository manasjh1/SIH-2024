const express = require("express");
const router= express.Router();
const contactForm=require("../controller/contact-controller");
const contactSchema=require("../validator/contact-validator");
const validate=require("../middlewares/contact-middleware");
router.route("/contact").post(validate(contactSchema),contactForm);
module.exports=router;