import { NavLink } from "react-router-dom";
import { Analytics } from "../components/Analytics";

export const About = () => {
  return (
    <>
      <main>
        <section className="section-hero">
          <div className="container grid grid-two-cols">
            <div className="hero-content">
              {/* <p>We care to cure your Health</p> */}

              <h1>Why Choose Us? </h1>
              <p>
              Choosing us means entrusting your legal needs to a team that combines experience, dedication, and a client-focused approach. We are committed to providing top-tier legal services, tailored to meet the unique challenges of each case. Our team of seasoned professionals brings deep expertise across various areas of law, ensuring that your legal matters are handled with the utmost competence and care. 
              </p>
              <p>
              We pride ourselves on our proactive approach, anticipating potential challenges and crafting innovative solutions that align with your goals.
              </p>
              <p>
              Transparency is at the core of our practice—we keep you informed at every stage, ensuring you understand your options and the potential outcomes. Our commitment to excellence extends beyond just winning cases; it’s about building lasting relationships based on trust, respect, and mutual success. 
              </p>
              <p>
              With us, you’ll receive not only exceptional legal representation but also the peace of mind that comes from knowing you have a dedicated team fighting for your rights and interests. Choose us because we are more than just legal professionals—we are your partners in achieving justice and securing a brighter future
              </p>
              <p>
                Reliability: Count on us to be there when you need us. We're
                committed to ensuring your IT environment is reliable and
                available 24/7.
              </p>
              <div className="btn btn-group">
                <NavLink to="/contact">
                  <button className="btn"> Connect Now</button>
                </NavLink>
                <button className="btn secondary-btn">learn more</button>
              </div>
            </div>
            <div className="hero-image">
              <img
                src="/images/about.png"
                alt="coding buddies "
                width="400"
                height="500"
              />
            </div>
          </div>
        </section>
      </main>

      <Analytics />
    </>
  );
};