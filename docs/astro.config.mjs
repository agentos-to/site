// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightThemeGalaxy from 'starlight-theme-galaxy';

// https://astro.build/config
export default defineConfig({
	site: 'https://agentos.to',
	base: '/docs',
	trailingSlash: 'always',
	build: { format: 'directory' },
	integrations: [
		starlight({
			title: 'AgentOS Docs',
			plugins: [starlightThemeGalaxy()],
			customCss: ['./src/styles/custom.css'],
			head: [
				{
					tag: 'script',
					content: `
						document.addEventListener('DOMContentLoaded', () => {
							const topUl = document.querySelector('nav[aria-label="Main"] ul.top-level');
							if (!topUl) return;
							const topLevel = Array.from(topUl.querySelectorAll(':scope > li > details'));
							const DURATION = 200;
							const EASING = 'cubic-bezier(0.22, 1, 0.36, 1)';

							// Animate a <details> open/close by measuring its body <ul>
							// and animating max-height. <details open> toggles are not
							// animatable natively, so we hijack the click.
							const animate = (details, shouldOpen) => {
								const body = details.querySelector(':scope > ul');
								if (!body) {
									details.open = shouldOpen;
									return;
								}
								details.dataset.animating = '1';
								if (shouldOpen) {
									details.open = true;
									const end = body.scrollHeight;
									body.style.overflow = 'hidden';
									const anim = body.animate(
										[{ maxHeight: '0px' }, { maxHeight: end + 'px' }],
										{ duration: DURATION, easing: EASING },
									);
									anim.onfinish = () => {
										body.style.overflow = '';
										delete details.dataset.animating;
									};
								} else {
									const start = body.scrollHeight;
									body.style.overflow = 'hidden';
									const anim = body.animate(
										[{ maxHeight: start + 'px' }, { maxHeight: '0px' }],
										{ duration: DURATION, easing: EASING },
									);
									anim.onfinish = () => {
										details.open = false;
										body.style.overflow = '';
										delete details.dataset.animating;
									};
								}
							};

							topLevel.forEach((d) => {
								const summary = d.querySelector(':scope > summary');
								if (!summary) return;
								summary.addEventListener('click', (e) => {
									e.preventDefault();
									if (d.dataset.animating) return;
									const willOpen = !d.open;
									// Close any siblings first, then open target in series
									if (willOpen) {
										const siblingsToClose = topLevel.filter((o) => o !== d && o.open);
										siblingsToClose.forEach((o) => animate(o, false));
										setTimeout(() => animate(d, true), siblingsToClose.length ? DURATION : 0);
									} else {
										animate(d, false);
									}
								});
							});
						});
					`,
				},
			],
			sidebar: [
				{
					label: 'Introduction',
					collapsed: true,
					items: [
						{ label: 'What is AgentOS', slug: 'introduction/what-is-agentos' },
						{ label: 'Vision', slug: 'introduction/vision' },
						{ label: 'Inspiration', slug: 'introduction/inspiration' },
						{ label: 'The two users', slug: 'introduction/two-users' },
					],
				},
				{
					label: 'Principles',
					collapsed: true,
					items: [
						{ label: 'Design principles', slug: 'principles/design-principles' },
						{ label: 'Architectural laws', slug: 'principles/architectural-laws' },
						{ label: 'Agent empathy', slug: 'principles/agent-empathy' },
						{ label: 'How we build', slug: 'principles/how-we-build' },
						{ label: 'Roadmap & proposals', slug: 'principles/roadmap-and-proposals' },
					],
				},
				{
					label: 'Architecture',
					collapsed: true,
					items: [
						{ label: 'Overview', slug: 'architecture/overview' },
						{ label: 'Security', slug: 'architecture/security' },
						{ label: 'Local-first', slug: 'architecture/local-first' },
						{ label: 'Data model', slug: 'architecture/data-model' },
					],
				},
				{
					label: 'Shapes',
					collapsed: true,
					items: [
						{ label: 'Overview', slug: 'shapes/overview' },
						{ label: 'Shape design principles', slug: 'shapes/shape-design-principles' },
						{ label: 'Memex & the graph', slug: 'shapes/memex-and-graph' },
						{ label: 'Identity & change', slug: 'shapes/identity-and-change' },
						{ label: 'Reference', autogenerate: { directory: 'shapes/reference' }, collapsed: true },
					],
				},
				{
					label: 'Skills',
					collapsed: true,
					items: [
						{ label: 'Overview', slug: 'skills/overview' },
						{ label: 'Connections', slug: 'skills/connections' },
						{ label: 'Auth flows', slug: 'skills/auth-flows' },
						{ label: 'Data', slug: 'skills/data' },
						{ label: 'LLM', slug: 'skills/llm' },
						{
							label: 'Reverse engineering',
							collapsed: true,
							items: [
								{ label: 'Overview', slug: 'skills/reverse-engineering/overview' },
								{ label: '1. Transport', slug: 'skills/reverse-engineering/1-transport' },
								{ label: '2. Discovery', slug: 'skills/reverse-engineering/2-discovery' },
								{
									label: '3. Auth',
									collapsed: true,
									items: [
										{ label: 'Overview', slug: 'skills/reverse-engineering/3-auth/overview' },
										{ label: 'NextAuth', slug: 'skills/reverse-engineering/3-auth/nextauth' },
										{ label: 'WorkOS', slug: 'skills/reverse-engineering/3-auth/workos' },
										{ label: 'macOS Keychain', slug: 'skills/reverse-engineering/3-auth/macos-keychain' },
									],
								},
								{ label: '4. Content', slug: 'skills/reverse-engineering/4-content' },
								{ label: '5. Social', slug: 'skills/reverse-engineering/5-social' },
								{
									label: '6. Desktop apps',
									collapsed: true,
									items: [
										{ label: 'Overview', slug: 'skills/reverse-engineering/6-desktop-apps/overview' },
										{ label: 'Electron', slug: 'skills/reverse-engineering/6-desktop-apps/electron' },
									],
								},
								{ label: '7. MCP', slug: 'skills/reverse-engineering/7-mcp' },
							],
						},
						{
							label: 'Reference',
							collapsed: true,
							items: [
								{ label: 'Skills index', slug: 'skills/reference' },
								{ label: 'agents', autogenerate: { directory: 'skills/reference/agents' }, collapsed: true },
								{ label: 'ai', autogenerate: { directory: 'skills/reference/ai' }, collapsed: true },
								{ label: 'browsers', autogenerate: { directory: 'skills/reference/browsers' }, collapsed: true },
								{ label: 'comms', autogenerate: { directory: 'skills/reference/comms' }, collapsed: true },
								{ label: 'dev', autogenerate: { directory: 'skills/reference/dev' }, collapsed: true },
								{ label: 'finance', autogenerate: { directory: 'skills/reference/finance' }, collapsed: true },
								{ label: 'fun', autogenerate: { directory: 'skills/reference/fun' }, collapsed: true },
								{ label: 'hosting', autogenerate: { directory: 'skills/reference/hosting' }, collapsed: true },
								{ label: 'logistics', autogenerate: { directory: 'skills/reference/logistics' }, collapsed: true },
								{ label: 'macos', autogenerate: { directory: 'skills/reference/macos' }, collapsed: true },
								{ label: 'media', autogenerate: { directory: 'skills/reference/media' }, collapsed: true },
								{ label: 'productivity', autogenerate: { directory: 'skills/reference/productivity' }, collapsed: true },
								{ label: 'web', autogenerate: { directory: 'skills/reference/web' }, collapsed: true },
							],
						},
					],
				},
				{
					label: 'Apps',
					collapsed: true,
					items: [
						{ label: 'Overview', slug: 'apps/overview' },
					],
				},
				{
					label: 'Research',
					collapsed: true,
					items: [
						{ label: 'Ontology', autogenerate: { directory: 'research/ontology' }, collapsed: true },
						{ label: 'Platforms', autogenerate: { directory: 'research/platforms' }, collapsed: true },
						{ label: 'Identity & spaces', autogenerate: { directory: 'research/identity-and-spaces' }, collapsed: true },
						{ label: 'Relationships & events', autogenerate: { directory: 'research/relationships-and-events' }, collapsed: true },
						{ label: 'Context & ecosystem', autogenerate: { directory: 'research/context' }, collapsed: true },
						{ label: 'DX patterns', autogenerate: { directory: 'research/dx-patterns' }, collapsed: true },
					],
				},
			],
		}),
	],
});
