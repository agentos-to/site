// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightThemeGalaxy from 'starlight-theme-galaxy';
import starlightSidebarTopics from 'starlight-sidebar-topics';

// Reference docs (shapes, apps, ops, tool surface) are no longer pages here —
// they live on the System Docs volume, projected from the canonical source
// (ontology YAML, rustdoc, ts-morph, the tool registry). This site keeps
// only the human narrative. See core/_roadmap/p2/system-volume/plan.md.

// https://astro.build/config
export default defineConfig({
	site: 'https://agentos.to',
	trailingSlash: 'always',
	build: { format: 'directory' },
	integrations: [
		starlight({
			title: 'AgentOS Docs',
			components: {
				Header: './src/components/Header.astro',
			},
			plugins: [
				starlightThemeGalaxy(),
				starlightSidebarTopics([
					{
						label: 'Learn',
						link: '/introduction/what-is-agentos/',
						icon: 'open-book',
						items: [
							{
								label: 'Introduction',
								collapsed: false,
								items: [
									{ label: 'What is AgentOS', slug: 'introduction/what-is-agentos' },
									{ label: 'Inspiration', slug: 'introduction/inspiration' },
									{ label: 'The two users', slug: 'introduction/two-users' },
									{ label: 'Roadmap & proposals', slug: 'introduction/roadmap-and-proposals' },
								],
							},
						],
					},
					{
						id: 'build',
						label: 'Build',
						link: '/introduction/how-we-build/',
						icon: 'puzzle',
						items: [
							{
								label: 'Build discipline',
								collapsed: false,
								items: [
									{ label: 'How we build', slug: 'introduction/how-we-build' },
								],
							},
							{
								label: 'Architecture',
								collapsed: false,
								items: [
									{ label: 'Overview', slug: 'architecture/overview' },
									{ label: 'Design principles', slug: 'architecture/design-principles' },
									{ label: 'Architectural laws', slug: 'architecture/architectural-laws' },
									{ label: 'Security', slug: 'architecture/security' },
									{ label: 'Local-first', slug: 'architecture/local-first' },
									{ label: 'Data model', slug: 'architecture/data-model' },
									{ label: 'App dispatch', slug: 'architecture/app-dispatch' },
									{ label: 'Connections as browsers', slug: 'architecture/connections-as-browsers' },
									{ label: 'Auth resolution', slug: 'architecture/auth-resolution' },
									{ label: 'Observer bus', slug: 'architecture/observer-bus' },
									{ label: 'Shape extraction', slug: 'architecture/shape-extraction' },
									{ label: 'Response shaping', slug: 'architecture/response-shaping' },
									{ label: 'View prefs', slug: 'architecture/view-prefs' },
								],
							},
							{
								label: 'Interfaces',
								collapsed: false,
								items: [
									{ label: 'Overview', slug: 'interfaces/overview' },
									{ label: 'MCP', slug: 'interfaces/mcp' },
									{ label: 'CLI', slug: 'interfaces/cli' },
									{ label: 'HTTP', slug: 'interfaces/http' },
								],
							},
							{
								label: 'Apps',
								collapsed: false,
								items: [
									{ label: 'Overview', slug: 'apps/overview' },
									{ label: 'Agent empathy', slug: 'apps/agent-empathy' },
									{ label: 'Connections', slug: 'apps/connections' },
									{ label: 'Auth flows', slug: 'apps/auth-flows' },
									{ label: 'Data', slug: 'apps/data' },
									{ label: 'LLM', slug: 'apps/llm' },
									{ label: 'Adding login', slug: 'apps/adding-login' },
								],
							},
							{
								label: 'Reverse engineering',
								collapsed: false,
								items: [
									{ label: 'Overview', slug: 'apps/reverse-engineering/overview' },
									{ label: '1. Transport', slug: 'apps/reverse-engineering/1-transport' },
									{ label: '2. Discovery', slug: 'apps/reverse-engineering/2-discovery' },
									{ label: '3. Auth', slug: 'apps/reverse-engineering/3-auth/overview' },
									{ label: '4. Content', slug: 'apps/reverse-engineering/4-content' },
									{ label: '5. Social', slug: 'apps/reverse-engineering/5-social' },
									{ label: '6. Desktop apps', slug: 'apps/reverse-engineering/6-desktop-apps/overview' },
									{ label: '7. MCP', slug: 'apps/reverse-engineering/7-mcp' },
								],
							},
						],
					},
					{
						id: 'shapes',
						label: 'Shapes',
						link: '/shapes/overview/',
						icon: 'seti:crystal',
						items: [
							{
								label: 'Shapes',
								collapsed: false,
								items: [
									{ label: 'Overview', slug: 'shapes/overview' },
									{ label: 'Shape design principles', slug: 'shapes/shape-design-principles' },
									{ label: 'Memex & the graph', slug: 'shapes/memex-and-graph' },
									{ label: 'Identity & change', slug: 'shapes/identity-and-change' },
								],
							},
						],
					},
					{
						label: 'Research',
						link: '/research/ontology/relationship-modeling/',
						icon: 'document',
						items: [
							{ label: 'Ontology', autogenerate: { directory: 'research/ontology' }, collapsed: false },
							{ label: 'Platforms', autogenerate: { directory: 'research/platforms' }, collapsed: false },
							{ label: 'Identity & spaces', autogenerate: { directory: 'research/identity-and-spaces' }, collapsed: false },
							{ label: 'Relationships & events', autogenerate: { directory: 'research/relationships-and-events' }, collapsed: false },
							{ label: 'Context & ecosystem', autogenerate: { directory: 'research/context' }, collapsed: false },
							{ label: 'DX patterns', autogenerate: { directory: 'research/dx-patterns' }, collapsed: false },
							{ label: 'Interfaces', autogenerate: { directory: 'research/interfaces' }, collapsed: false },
						],
					},
				], {
					topics: {
						build: [
							'/apps/reverse-engineering/3-auth/*',
							'/apps/reverse-engineering/6-desktop-apps/*',
						],
					},
				}),
			],
			customCss: ['./src/styles/custom.css'],
			head: [
				{
					tag: 'script',
					attrs: { type: 'module' },
					content: `
						import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';

						// Starlight renders code fences through Expressive Code, which wraps
						// content in .expressive-code > pre > code.language-mermaid and applies
						// syntax-highlight styles. Unwrap those to plain <pre class="mermaid">text</pre>
						// so mermaid can run on the raw source.
						const render = () => {
							const blocks = document.querySelectorAll('code.language-mermaid');
							if (!blocks.length) return;
							blocks.forEach((code) => {
								const wrapper = code.closest('.expressive-code') || code.closest('pre');
								if (!wrapper || wrapper.dataset.mermaidMounted === '1') return;
								const pre = document.createElement('pre');
								pre.className = 'mermaid';
								pre.textContent = code.textContent;
								wrapper.replaceWith(pre);
								pre.dataset.mermaidMounted = '1';
							});
							const isDark = document.documentElement.dataset.theme !== 'light';
							mermaid.initialize({
								startOnLoad: false,
								theme: isDark ? 'dark' : 'default',
								securityLevel: 'loose',
								themeVariables: isDark ? {
									background: '#0b0b0f',
									primaryColor: '#1a1a24',
									primaryTextColor: '#e8e8ee',
									primaryBorderColor: '#3d3d4d',
									lineColor: '#8b8b98',
									secondaryColor: '#141420',
									tertiaryColor: '#101018',
								} : {},
							});
							mermaid.run({ querySelector: 'pre.mermaid:not([data-processed])' });
						};

						if (document.readyState === 'loading') {
							document.addEventListener('DOMContentLoaded', render);
						} else {
							render();
						}

						// Re-run on Astro view transitions
						document.addEventListener('astro:after-swap', render);
					`,
				},
			],
		}),
	],
});
