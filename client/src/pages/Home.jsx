import { Analytics } from "../components/Analytics";
export const Home=()=>{
    return <>
        <main>
            <section className="section-hero">
                <div className="container grid grid-two-cols">
                    <div className="hero-content">
                        <p> We the people of INDIA</p>
                        <h1>welcome to trial phase of Indian Gov. Site</h1>
                        <p> Welcome to the official portal for India Judicial Courts, your gateway to accessing fair and impartial justice. We manage all judicial processes, from local courts to the Supreme Court, ensuring adherence to constitutional principles. Our site provides essential legal resources, including case filings, court schedules, and updates on legal developments, promoting transparency and public trust in the judicial system.
                        </p>
                        <div className="btn-btn-group">
                            <a href="/contact">
                                <button className="btn">Connect Now</button>
                            </a>
                            <a href="/service">
                                <button className="btn secondary-btn">learn more</button>
                            </a>
                        </div>
                    </div>
                     <div className="hero-image">
                        <img src="/images/home.png" alt="home page image" width="300px" height="400px" />
                    </div>
                </div>
               
            </section>
        </main>
        {/* 2nd Section*/}
        <Analytics />
        {/*3rd section */}
        <section className="section-hero">
            <div className="container grid grid-two-cols">
                <div className="hero-image">
                    <img src="/images/info.png" alt="home page image" width="300px" height="400px" />
                </div>
                <div className="hero-content">
                        <p> Indeed the LAW</p>
                        <h1>welecome to trial phase one</h1>
                        <p> We are committed to enhancing public trust in the legal system by promoting accountability and ensuring that all judicial actions are in strict adherence to the Constitution. Our website serves as a bridge between the government and the public, fostering greater awareness of legal rights and responsibilities while streamlining access to justice. Explore our resources to stay informed about ongoing cases, landmark judgments, and the latest developments in the legal landscape of INDIA.
                            unique needs.
                        </p>
                        <div className="btn-btn-group">
                            <a href="/contact">
                                <button className="btn">Connect Now</button>
                            </a>
                            <a href="/service">
                                <button className="btn secondary-btn">learn more</button>
                            </a>
                        </div>
                    </div>
            </div>
        </section>
    </>
};