import React from "react";
import "./Home.css";
import Product from "./Product";


export default function Home() { 
  return(
  <div className="home">
      <div className="home__container">
          <img className= "home__image"
          src="https://images-na.ssl-images-amazon.com/images/G/01/credit/img20/CBCC/CE/CBCC_Prime_ACQ_GW_Hero_CV8_1500x600_1X._CB669137065_.jpg" alt="amazon pic"/>  
      

            <div className="home__row">
                <Product  
                id="1"
                title='PASSY: The compact Passy handbag in Monogram canvas with a sliding chain is the quintessence of casual chic.' 
                price={19.99}  
                image='https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-passy-monogram-handbags--M45592_PM2_Front%20view.png?wid=2048&hei=2048' 
                rating={5} />

                <Product  
                id="2"
                title='PETIT SAC PLAT: This Architettura special edition of the iconic Petit Sac Plat was inspired by Artistic Director Nicolas Ghesquières' 
                price={19.99}  
                image='https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-petit-sac-plat-other-leathers-small-leather-goods--M80991_PM2_Front%20view.png?wid=2048&hei=2048' 
                rating={5} />
            </div>

            <div className="home__row">
            <Product  
                id="3"
                title='PETIT SAC PLAT: The Petit Sac Plat is crafted from supple, grained Monogram Empreinte leather with the embossed Monogram pattern highlighted by the chic bicolor palette.' 
                price={19.99}  
                image='https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-petit-sac-plat-bicolor-monogram-empreinte-leather-small-leather-goods--M57937_PM2_Front%20view.png?wid=2048&hei=2048' 
                rating={5} />

                <Product  
                id="4"
                title='Inspired by the House’s historic Sac Plat, the Sac Plat BB is made from grained Epi leather with smooth calf leather on the gussets.' 
                price={19.99}  
                image='https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-sac-plat-bb-epi-leather-handbags--M58659_PM2_Front%20view.png?wid=2048&hei=2048' 
                rating={3} />

                <Product  
                id="5"
                title='NEVERFULL MM: Part of the LVxFornasetti capsule collection created for the Fall-Winter 2021 season' 
                price={19.99}  
                image='https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-neverfull-mm-monogram-handbags--M45923_PM2_Front%20view.png?wid=2048&hei=2048' 
                rating={2} />

            </div>

            <div className="home__row">
                <Product  
                id="6"
                title='TROCA PM: Designed for day-to-evening use, the small Troca PM handbag is made from Damier Quilt, padded lambskin with a large checkerboard Damier pattern.' 
                price={19.99}  
                image='https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-troca-pm-h27-handbags--M59118_PM2_Front%20view.png?wid=2048&hei=2048' 
                rating={5} />
            </div>
      </div> 
  </div>

  );
}
