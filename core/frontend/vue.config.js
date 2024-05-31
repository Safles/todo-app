module.exports = {
    devServer: {
        proxy: 'http://127.0.0.1:8000/'
    },
    plugins: [
          require('unplugin-vue-components/webpack').default({ /* options */ }),
        ],
}