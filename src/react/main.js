// Reactのバージョンを定義
const version = "19.1.0";

// アプリケーションの初期化を行う非同期関数
/* async function init() {
    // Reactのコアライブラリを動的にインポート
    const module1 = await import(`https://esm.sh/react@${version}`);
    // グローバルスコープにReactを設定
    window.React = module1.default;
    // ReactDOMクライアントを動的にインポート
    const module2 = await import(`https://esm.sh/react-dom@${version}/client`);
    // グローバルスコープにReactDOMClientを設定
    window.ReactDOMClient = module2.default;

    // メイン処理を実行
    main();
}
 */

function init() {
    import(`https://esm.sh/react@${version}`).then(React => {
        window.React = React;
        import(`https://esm.sh/react-dom@${version}/client/?dev`)
            .   then(ReactDOMClient => {
            window.ReactDOMClient = ReactDOMClient;
            main();
        });
    });
}

// アプリケーションのメイン処理を行う関数
function main() {
    // DOMからルート要素を取得
    const root = document.getElementById("root");
    // Reactのルート要素を作成
    const rootElement = ReactDOMClient.createRoot(root);
    // h2要素を作成
    const h2 = React.createElement("h2", {}, "Sample application");
    // p要素を作成
    const p = React.createElement("p", {}, "これはReactのサンプルアプリケーションです。");
    // div要素を作成し、その中にh2とpを配置
    const div = React.createElement("p", {}, [h2, p]);
    // 作成した要素を画面に描画
    rootElement.render(div);
}

// アプリケーションを初期化して実行
init();