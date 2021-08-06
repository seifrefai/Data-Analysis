import React from 'react'
import './Product.css'
function Product({id,title,price,image,rating}) {
    return (
        <div className= "product">
            <div className="product__info">
                <p>{title}</p>
                <p className="product__price">
                <small>$</small>
                <strong>{price}</strong>
                </p>

                <div className= "product__rating">
                    {Array(rating).fill().map(i => (<p>🌟</p>))}

                </div>  
            </div>


                <img src={image} alt="loui" />

                <button className="product__button">Add to basket</button>
           
        </div>
    )
}

export default Product
