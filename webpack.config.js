const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = (env, options) => {
  let output_path = '/src/static/build/';
  if (options.mode === 'production') {
    output_path = '/src/static/dist/';
  }

  return {
    entry: './src/static/src/js/index.tsx',
    resolve: {
      extensions: ['.ts', '.tsx', '.js']
    },
    output: {
      path: path.join(__dirname, output_path),
      filename: "[name]-[hash].js"
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
      new BundleTracker({
        filename: './src/static/webpack-stats.json'
      })
    ]
  };
};
