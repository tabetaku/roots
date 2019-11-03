const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
console.log(__dirname);
module.exports = {
  entry: './src/static/src/js/index.tsx',
  resolve: {
    extensions: ['.ts', '.tsx', '.js']
  },
  output: {
    path: path.join(__dirname, '/src/static/dist'),
    filename: 'bundle.min.js'
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        loader: 'awesome-typescript-loader'
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/static/src/index.html'
    })
  ]
};
