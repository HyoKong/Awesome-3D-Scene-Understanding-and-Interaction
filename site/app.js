(() => {
  "use strict";

  const PAGE_SIZE = 24;
  const root = document.documentElement;

  function init() {
    initSurveyNavigation();
    initDeferredVideo();
    const form = document.querySelector("#paper-filters");
    const search = document.querySelector("#paper-search");
    const topicFilters = document.querySelector("#topic-filters");
    const topicButtons = [...document.querySelectorAll("#topic-filters button[data-topic]")];
    const year = document.querySelector("#paper-year");
    const order = document.querySelector("#paper-order");
    const hasCode = document.querySelector("#has-code");
    const reset = document.querySelector("#reset-filters");
    const resultsCount = document.querySelector("#results-count");
    const list = document.querySelector("#paper-list");
    const empty = document.querySelector("#empty-state");
    const loadMore = document.querySelector("#load-more");

    if (!form || !search || !topicFilters || !year || !order || !hasCode || !reset ||
        !resultsCount || !list || !empty || !loadMore) return;

    const papers = [...list.querySelectorAll(".paper-item")];
    let visibleLimit = PAGE_SIZE;
    let state = { q: "", topic: "", year: "", code: false, sort: "newest" };

    root.classList.add("js");

    function normalizeQuery(value) {
      return value.trim().replace(/\s+/g, " ").toLocaleLowerCase();
    }

    function stateFromUrl() {
      const params = new URLSearchParams(window.location.search);
      const permittedTopics = new Set(topicButtons.map((button) => button.dataset.topic || ""));
      const permittedYears = new Set([...year.options].map((option) => option.value));
      const requestedSort = params.get("sort");
      return {
        q: normalizeQuery(params.get("q") || ""),
        topic: permittedTopics.has(params.get("topic") || "") ? (params.get("topic") || "") : "",
        year: permittedYears.has(params.get("year") || "") ? (params.get("year") || "") : "",
        code: params.get("code") === "1",
        sort: ["newest", "oldest", "title"].includes(requestedSort) ? requestedSort : "newest",
      };
    }

    function syncControls() {
      if (search.value !== state.q) search.value = state.q;
      year.value = state.year;
      order.value = state.sort;
      hasCode.checked = state.code;
      for (const button of topicButtons) {
        button.setAttribute("aria-pressed", String((button.dataset.topic || "") === state.topic));
      }
    }

    function syncUrl() {
      const params = new URLSearchParams();
      const query = normalizeQuery(state.q);
      if (query) params.set("q", query);
      if (state.topic) params.set("topic", state.topic);
      if (state.year) params.set("year", state.year);
      if (state.code) params.set("code", "1");
      if (state.sort !== "newest") params.set("sort", state.sort);
      const serialized = params.toString();
      const next = `${window.location.pathname}${serialized ? `?${serialized}` : ""}${window.location.hash}`;
      window.history.replaceState(null, "", next);
    }

    function matchingPapers() {
      const tokens = normalizeQuery(state.q).split(/\s+/).filter(Boolean);
      const matching = papers.filter((paper) => {
        const topics = (paper.dataset.topics || "").split(/\s+/);
        const paperYear = paper.dataset.year || "";
        const searchable = paper.dataset.search || "";
        return (!state.topic || topics.includes(state.topic)) &&
          (!state.year || paperYear === state.year) &&
          (!state.code || paper.dataset.code === "released") &&
          tokens.every((token) => searchable.includes(token));
      });
      return matching.sort((first, second) => {
        const firstYear = Number(first.dataset.year || 0);
        const secondYear = Number(second.dataset.year || 0);
        const titleOrder = (first.dataset.title || "").localeCompare(second.dataset.title || "");
        if (state.sort === "title") return titleOrder;
        if (state.sort === "oldest") return firstYear - secondYear || titleOrder;
        return secondYear - firstYear || titleOrder;
      });
    }

    function render({ updateUrl = true } = {}) {
      const matches = matchingPapers();
      const showCount = Math.min(visibleLimit, matches.length);
      const showing = new Set(matches.slice(0, showCount));
      for (const paper of papers) paper.hidden = !showing.has(paper);
      for (const paper of matches.slice(0, showCount)) list.append(paper);

      empty.hidden = matches.length !== 0;
      loadMore.hidden = showCount >= matches.length;
      loadMore.textContent = `Show ${Math.min(PAGE_SIZE, matches.length - showCount)} more papers`;
      resultsCount.textContent = matches.length === papers.length
        ? `${papers.length} papers`
        : `${matches.length} of ${papers.length} papers`;
      syncControls();
      if (updateUrl) syncUrl();
      return matches;
    }

    function readControls() {
      state.q = search.value;
      state.year = year.value;
      state.sort = order.value;
      state.code = hasCode.checked;
      visibleLimit = PAGE_SIZE;
      render();
    }

    function focusPaper(id, { scroll = true } = {}) {
      const paper = document.getElementById(id);
      if (!paper || !paper.classList.contains("paper-item")) return false;
      const matches = matchingPapers();
      const index = matches.indexOf(paper);
      if (index === -1) {
        state = { q: "", topic: "", year: "", code: false, sort: "newest" };
        visibleLimit = PAGE_SIZE;
      }
      const refreshed = index === -1 ? matchingPapers() : matches;
      visibleLimit = Math.max(visibleLimit, refreshed.indexOf(paper) + 1);
      render();
      const heading = paper.querySelector("h1, h2, h3, h4") || paper;
      heading.setAttribute("tabindex", "-1");
      if (scroll) heading.focus({ preventScroll: true });
      if (scroll) {
        const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        paper.scrollIntoView({ behavior: reducedMotion ? "auto" : "smooth", block: "start" });
      }
      return true;
    }

    function revealHash({ scroll = true } = {}) {
      let id = "";
      try {
        id = decodeURIComponent(window.location.hash.slice(1));
      } catch {
        return;
      }
      if (id) focusPaper(id, { scroll });
    }

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      readControls();
    });
    search.addEventListener("input", readControls);
    year.addEventListener("change", readControls);
    order.addEventListener("change", readControls);
    hasCode.addEventListener("change", readControls);
    topicFilters.addEventListener("click", (event) => {
      const button = event.target.closest("button[data-topic]");
      if (!button) return;
      state.topic = button.dataset.topic || "";
      visibleLimit = PAGE_SIZE;
      render();
    });
    reset.addEventListener("click", () => {
      state = { q: "", topic: "", year: "", code: false, sort: "newest" };
      visibleLimit = PAGE_SIZE;
      render();
      search.focus();
    });
    loadMore.addEventListener("click", () => {
      visibleLimit += PAGE_SIZE;
      render();
    });
    document.addEventListener("click", (event) => {
      const link = event.target.closest('a[href^="#paper-"]');
      if (!link) return;
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
      let id = "";
      try {
        id = decodeURIComponent(link.getAttribute("href").slice(1));
      } catch {
        return;
      }
      if (!document.getElementById(id)) return;
      event.preventDefault();
      if (window.location.hash !== `#${id}`) window.history.pushState(null, "", `#${id}`);
      focusPaper(id);
    });
    window.addEventListener("hashchange", () => revealHash());
    window.addEventListener("popstate", () => {
      state = stateFromUrl();
      visibleLimit = PAGE_SIZE;
      render({ updateUrl: false });
      revealHash();
    });

    state = stateFromUrl();
    render({ updateUrl: false });
    revealHash({ scroll: false });
  }

  function initDeferredVideo() {
    for (const button of document.querySelectorAll(".media-consent[data-youtube-src]")) {
      button.addEventListener("click", () => {
        const src = button.dataset.youtubeSrc || "";
        let url;
        try { url = new URL(src); } catch { return; }
        if (url.protocol !== "https:" || !/(^|\.)youtube-nocookie\.com$/.test(url.hostname)) return;
        url.searchParams.set("autoplay", "1");
        const frame = document.createElement("iframe");
        frame.src = url.toString();
        frame.title = button.closest(".paper-media")?.querySelector("figcaption strong")?.textContent || "Official video";
        frame.loading = "lazy";
        frame.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
        frame.allowFullscreen = true;
        button.replaceWith(frame);
      }, { once: true });
    }
  }

  function initSurveyNavigation() {
    const toc = document.querySelector(".survey-toc nav");
    const chapters = [...document.querySelectorAll(".survey-chapter[id]")];
    if (!toc || !chapters.length || !("IntersectionObserver" in window)) return;
    const links = new Map([...toc.querySelectorAll('a[href^="#chapter-"]')].map((link) => [link.getAttribute("href").slice(1), link]));
    const setActive = (id) => {
      for (const [chapterId, link] of links) link.classList.toggle("is-active", chapterId === id);
    };
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (visible) setActive(visible.target.id);
    }, { rootMargin: "-20% 0px -68% 0px", threshold: 0 });
    chapters.forEach((chapter) => observer.observe(chapter));
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
