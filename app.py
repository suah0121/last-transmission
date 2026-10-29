import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="LAST TRANSMISSION",
    page_icon="⌁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background: #050607 !important;
        color: #d8e0e5 !important;
    }

    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stSidebar"],
    footer {
        display: none !important;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    iframe {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #050607;
    color: #dce3e8;
    font-family: Consolas, "Courier New", monospace;
    overflow: hidden;
}

.desktop {
    position: relative;
    width: 100%;
    height: 100vh;
    min-height: 650px;
    background:
        radial-gradient(ellipse at 50% 45%, #101719 0%, #07090a 52%, #030405 100%);
    overflow: hidden;
}

.topbar {
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 22px;
    border-bottom: 1px solid #252c2f;
    background: rgba(5, 7, 8, .92);
    font-size: 11px;
    letter-spacing: 2px;
    color: #9caeb4;
}

.brand {
    color: #dce7e9;
    font-weight: bold;
}

.status {
    color: #70d7c4;
}

.window {
    position: absolute;
    display: flex;
    flex-direction: column;
    background: #c8cacc;
    color: #15191b;
    border: 1px solid #697175;
    box-shadow: 0 18px 55px rgba(0, 0, 0, .6);
    min-width: 290px;
    min-height: 180px;
    resize: both;
    overflow: hidden;
}

.titlebar {
    flex: 0 0 34px;
    height: 34px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-left: 12px;
    background: #aeb2b4;
    border-bottom: 1px solid #777e81;
    cursor: grab;
    user-select: none;
    font-family: Arial, sans-serif;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: .5px;
}

.titlebar:active {
    cursor: grabbing;
}

.window-controls {
    height: 100%;
    display: flex;
    align-items: stretch;
}

.control {
    width: 35px;
    border: 0;
    border-left: 1px solid #929799;
    background: #b9bdbe;
    color: #202426;
    font-size: 15px;
    cursor: pointer;
}

.control:hover {
    background: #e0e2e3;
}

.control.close {
    background: #d94b4b;
    color: white;
    border-left-color: #b83b3b;
}

.control.close:hover {
    background: #f05a5a;
}

.window-content {
    flex: 1;
    min-height: 0;
    overflow: auto;
}

#home {
    left: 5%;
    top: 125px;
    width: 57%;
    height: 500px;
    z-index: 2;
}

#terminal {
    left: 43%;
    top: 205px;
    width: 49%;
    height: 390px;
    z-index: 3;
    background: #090d0f;
    color: #d8e4e7;
    border-color: #455257;
}

#terminal .titlebar {
    background: #333a3d;
    color: #dce3e5;
    border-bottom-color: #50595d;
}

#terminal .control {
    background: #3d4548;
    color: #e5eaeb;
    border-left-color: #525b5e;
}

#terminal .control.close {
    background: #d94b4b;
}

#terminal .window-content {
    background:
        linear-gradient(rgba(255,255,255,.012) 1px, transparent 1px);
    background-size: 100% 4px;
    padding: 24px;
}

.terminal-heading {
    color: #77e0cc;
    font-size: 14px;
    letter-spacing: 1.5px;
    margin-bottom: 24px;
}

.terminal-line {
    font-size: 12px;
    line-height: 2;
    color: #b6c2c6;
}

.terminal-line .good {
    color: #78d9c7;
}

.terminal-message {
    margin-top: 28px;
    border-left: 2px solid #64d7c2;
    padding: 12px 14px;
    background: rgba(75, 190, 166, .06);
    color: #e2e8e9;
    font-family: Arial, sans-serif;
    font-size: 13px;
    line-height: 1.8;
}

.prompt {
    margin-top: 22px;
    color: #7fe3d0;
    font-size: 12px;
}

.cursor {
    display: inline-block;
    width: 7px;
    height: 13px;
    background: #78dfcb;
    vertical-align: -2px;
    animation: blink 1s steps(2, start) infinite;
}

@keyframes blink {
    to { visibility: hidden; }
}

.home-page {
    background: #f3f4f4;
    color: #202426;
    min-height: 100%;
    font-family: Arial, sans-serif;
}

.site-header {
    background: #ffffff;
    border-bottom: 1px solid #d8dcde;
    padding: 17px 22px 0;
}

.site-brand {
    font-size: 23px;
    font-weight: 800;
    letter-spacing: -1px;
}

.site-brand span {
    color: #178c83;
}

.site-subtitle {
    margin-top: 5px;
    font-size: 10px;
    color: #777f82;
    letter-spacing: 1px;
}

.nav {
    display: flex;
    gap: 26px;
    margin-top: 20px;
    height: 38px;
    align-items: center;
    border-top: 1px solid #eceeef;
}

.nav a {
    color: #303638;
    text-decoration: none;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: .5px;
}

.nav a:hover {
    color: #168f84;
}

.home-main {
    padding: 22px;
}

.section-label {
    font-size: 10px;
    color: #168f84;
    letter-spacing: 1.4px;
    font-weight: bold;
}

.headline {
    font-size: 23px;
    line-height: 1.4;
    margin: 10px 0;
    font-weight: 750;
    letter-spacing: -.8px;
}

.summary {
    color: #70797c;
    font-size: 12px;
    line-height: 1.8;
}

.news-grid {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 14px;
    margin-top: 24px;
}

.news-card {
    background: white;
    border: 1px solid #dfe3e4;
    padding: 15px;
    min-height: 130px;
}

.card-tag {
    color: #168f84;
    font-size: 9px;
    letter-spacing: 1px;
    font-weight: bold;
}

.card-title {
    margin-top: 10px;
    font-size: 14px;
    line-height: 1.5;
    font-weight: bold;
}

.card-text {
    margin-top: 7px;
    color: #778083;
    font-size: 11px;
    line-height: 1.6;
}

.community {
    margin-top: 14px;
    border-top: 1px solid #dfe3e4;
    padding-top: 16px;
}

.post {
    padding: 10px 0;
    border-bottom: 1px solid #e1e4e5;
    font-size: 11px;
    line-height: 1.7;
}

.post small {
    display: block;
    color: #879093;
    margin-bottom: 3px;
}

.footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 29px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 18px;
    border-top: 1px solid #252c2f;
    background: #080a0b;
    color: #78868a;
    font-size: 9px;
    letter-spacing: 1px;
}

.footer .online {
    color: #6bd5bd;
}

#desktop-message {
    display: none;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    color: #78868a;
    text-align: center;
    font-size: 12px;
    letter-spacing: 2px;
    line-height: 2;
}

@media (max-width: 700px) {
    .window {
        min-width: 260px;
    }

    #home {
        left: 3%;
        top: 90px;
        width: 76%;
        height: 420px;
    }

    #terminal {
        left: 20%;
        top: 300px;
        width: 77%;
        height: 330px;
    }

    .nav {
        gap: 13px;
    }

    .home-main {
        padding: 15px;
    }
}
</style>
</head>
<body>
<div class="desktop" id="desktop">

    <div class="topbar">
        <div class="brand">LAST TRANSMISSION</div>
        <div class="status">NODE-07 / CONNECTED</div>
    </div>

    <div id="desktop-message">
        <div>LAST TRANSMISSION</div>
        <div>SYSTEM WINDOW CLOSED</div>
        <div style="letter-spacing:1px">창을 닫았습니다. 페이지를 새로고침하면 초기 화면으로 돌아갑니다.</div>
    </div>

    <section class="window" id="home">
        <div class="titlebar">
            <span>HOME — CIVINET PUBLIC NETWORK</span>
            <div class="window-controls">
                <button class="control" data-action="min" title="최소화">−</button>
                <button class="control" data-action="max" title="최대화">□</button>
                <button class="control close" data-action="close" title="닫기">×</button>
            </div>
        </div>

        <div class="window-content">
            <div class="home-page">
                <header class="site-header">
                    <div class="site-brand">CIVI<span>NET</span></div>
                    <div class="site-subtitle">COMMUNITY INFORMATION NETWORK</div>
                    <nav class="nav">
                        <a href="#news">NEWS</a>
                        <a href="#community">COMMUNITY</a>
                        <a href="#map">MAP</a>
                        <a href="#radio">RADIO</a>
                    </nav>
                </header>

                <main class="home-main" id="news">
                    <div class="section-label">TODAY'S BRIEFING</div>
                    <div class="headline">도시 생활 정보와 지역 소식을<br>한곳에서 확인하세요.</div>
                    <div class="summary">
                        CIVINET은 지역 소식, 생활 정보와 커뮤니티 게시물을 제공하는
                        가상의 정보 네트워크입니다.
                    </div>

                    <div class="news-grid">
                        <article class="news-card">
                            <div class="card-tag">PUBLIC NOTICE</div>
                            <div class="card-title">이번 주 지역 생활 정보 안내</div>
                            <div class="card-text">
                                생활 편의시설 운영 정보와 지역 공지사항을 확인하세요.
                            </div>
                        </article>
                        <article class="news-card">
                            <div class="card-tag">NETWORK STATUS</div>
                            <div class="card-title">일부 정보 업데이트 지연</div>
                            <div class="card-text">
                                일부 게시물의 갱신이 평소보다 늦어질 수 있습니다.
                            </div>
                        </article>
                    </div>

                    <section class="community" id="community">
                        <div class="section-label">COMMUNITY / RECENT POSTS</div>
                        <div class="post">
                            <small>user_031 · 08:42</small>
                            오늘 아침부터 동네 게시판이 조금 느려진 것 같아요.
                        </div>
                        <div class="post">
                            <small>blue_window · 08:35</small>
                            공지 내용을 확인할 때 게시 날짜도 같이 보는 게 좋겠네요.
                        </div>
                        <div class="post">
                            <small>system_notice · 08:10</small>
                            일부 정보는 갱신 시점에 따라 실제 상황과 다를 수 있습니다.
                        </div>
                    </section>
                </main>
            </div>
        </div>
    </section>

    <section class="window" id="terminal">
        <div class="titlebar">
            <span>TERMINAL — NODE-07</span>
            <div class="window-controls">
                <button class="control" data-action="min" title="최소화">−</button>
                <button class="control" data-action="max" title="최대화">□</button>
                <button class="control close" data-action="close" title="닫기">×</button>
            </div>
        </div>

        <div class="window-content">
            <div class="terminal-heading">LAST TRANSMISSION // NODE-07</div>
            <div class="terminal-line">SYSTEM STATUS: <span class="good">ACTIVE</span></div>
            <div class="terminal-line">CONNECTION: <span class="good">ESTABLISHED</span></div>
            <div class="terminal-line">CHANNEL: ENCRYPTED / LOCAL</div>
            <div class="terminal-line">INCOMING TRANSMISSION DETECTED</div>

            <div class="terminal-message">
                접속이 확인되었습니다.<br>
                현재 전달된 메시지를 확인하십시오.<br>
                <span style="color:#83dfcf">모든 기록은 훈련용 가상 시나리오입니다.</span>
            </div>

            <div class="prompt">&gt; AWAITING INPUT<span class="cursor"></span></div>
        </div>
    </section>

    <div class="footer">
        <span>SESSION: LT-07-LOCAL</span>
        <span class="online">● SYSTEM READY</span>
        <span>SIMULATION BUILD 0.1</span>
    </div>
</div>

<script>
const desktop = document.getElementById("desktop");
const message = document.getElementById("desktop-message");
let highestZ = 5;

function focusWindow(win) {
    highestZ += 1;
    win.style.zIndex = highestZ;
}

document.querySelectorAll(".window").forEach(win => {
    const bar = win.querySelector(".titlebar");
    let dragging = false;
    let startX = 0, startY = 0, originX = 0, originY = 0;

    win.addEventListener("pointerdown", () => focusWindow(win));

    bar.addEventListener("pointerdown", event => {
        if (event.target.closest("button")) return;
        if (win.dataset.maximized === "true") return;

        dragging = true;
        startX = event.clientX;
        startY = event.clientY;
        originX = win.offsetLeft;
        originY = win.offsetTop;

        bar.setPointerCapture(event.pointerId);
    });

    bar.addEventListener("pointermove", event => {
        if (!dragging) return;

        const x = originX + event.clientX - startX;
        const y = originY + event.clientY - startY;

        win.style.left = Math.max(0, x) + "px";
        win.style.top = Math.max(42, y) + "px";
        win.style.right = "auto";
        win.style.bottom = "auto";
    });

    bar.addEventListener("pointerup", () => {
        dragging = false;
    });

    bar.addEventListener("pointercancel", () => {
        dragging = false;
    });

    win.querySelectorAll("button").forEach(button => {
        button.addEventListener("click", () => {
            const action = button.dataset.action;

            if (action === "close") {
                win.style.display = "none";
                checkEmptyDesktop();
            }

            if (action === "min") {
                win.style.display = "none";
                checkEmptyDesktop();
            }

            if (action === "max") {
                if (win.dataset.maximized === "true") {
                    win.style.left = win.dataset.oldLeft;
                    win.style.top = win.dataset.oldTop;
                    win.style.width = win.dataset.oldWidth;
                    win.style.height = win.dataset.oldHeight;
                    win.dataset.maximized = "false";
                } else {
                    win.dataset.oldLeft = win.style.left || win.offsetLeft + "px";
                    win.dataset.oldTop = win.style.top || win.offsetTop + "px";
                    win.dataset.oldWidth = win.style.width || win.offsetWidth + "px";
                    win.dataset.oldHeight = win.style.height || win.offsetHeight + "px";

                    win.style.left = "10px";
                    win.style.top = "52px";
                    win.style.width = "calc(100% - 20px)";
                    win.style.height = "calc(100% - 92px)";
                    win.dataset.maximized = "true";
                }
                focusWindow(win);
            }
        });
    });
});

function checkEmptyDesktop() {
    const windows = [...document.querySelectorAll(".window")];
    const visible = windows.some(win => win.style.display !== "none");
    message.style.display = visible ? "none" : "block";
}
</script>
</body>
</html>
""", height=900, scrolling=False)
