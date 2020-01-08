//laod babel loader here
module.exports = {
    module: {
        rules:[
            {
                test:/\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
}