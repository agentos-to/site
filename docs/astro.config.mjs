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
			sidebar: [
				{
					label: 'Introduction',
					collapsed: true,
					items: [
						{ label: 'What is AgentOS', slug: 'introduction/what-is-agentos' },
						{ label: 'Vision', slug: 'introduction/vision' },
						{ label: 'Inspiration', slug: 'introduction/inspiration' },
						{ label: 'The two users', slug: 'introduction/two-users' },
						{ label: 'Local-first', slug: 'introduction/local-first' },
					],
				},
				{
					label: 'Principles',
					collapsed: true,
					items: [
						{ label: 'Design principles', slug: 'principles/design-principles' },
						{ label: 'Architectural laws', slug: 'principles/architectural-laws' },
						{ label: 'Agent empathy', slug: 'principles/agent-empathy' },
					],
				},
				{
					label: 'Ontology',
					collapsed: true,
					items: [
						{ label: 'Overview', slug: 'ontology/overview' },
						{ label: 'Shape design principles', slug: 'ontology/shape-design-principles' },
						{ label: 'Memex & the graph', slug: 'ontology/memex-and-graph' },
						{ label: 'Identity & change', slug: 'ontology/identity-and-change' },
					],
				},
				{
					label: 'Contributing',
					collapsed: true,
					items: [
						{ label: 'How we build', slug: 'contributing/how-we-build' },
						{
							label: 'Skills',
							collapsed: true,
							items: [
								{ label: 'Overview', slug: 'contributing/skills/overview' },
								{ label: 'Connections', slug: 'contributing/skills/connections' },
								{ label: 'Auth flows', slug: 'contributing/skills/auth-flows' },
								{ label: 'Data', slug: 'contributing/skills/data' },
								{ label: 'LLM', slug: 'contributing/skills/llm' },
								{
									label: 'Reverse engineering',
									collapsed: true,
									items: [
										{ label: 'Overview', slug: 'contributing/skills/reverse-engineering/overview' },
										{ label: '1. Transport', slug: 'contributing/skills/reverse-engineering/1-transport' },
										{ label: '2. Discovery', slug: 'contributing/skills/reverse-engineering/2-discovery' },
										{
											label: '3. Auth',
											collapsed: true,
											items: [
												{ label: 'Overview', slug: 'contributing/skills/reverse-engineering/3-auth/overview' },
												{ label: 'NextAuth', slug: 'contributing/skills/reverse-engineering/3-auth/nextauth' },
												{ label: 'WorkOS', slug: 'contributing/skills/reverse-engineering/3-auth/workos' },
												{ label: 'macOS Keychain', slug: 'contributing/skills/reverse-engineering/3-auth/macos-keychain' },
											],
										},
										{ label: '4. Content', slug: 'contributing/skills/reverse-engineering/4-content' },
										{ label: '5. Social', slug: 'contributing/skills/reverse-engineering/5-social' },
										{
											label: '6. Desktop apps',
											collapsed: true,
											items: [
												{ label: 'Overview', slug: 'contributing/skills/reverse-engineering/6-desktop-apps/overview' },
												{ label: 'Electron', slug: 'contributing/skills/reverse-engineering/6-desktop-apps/electron' },
											],
										},
										{ label: '7. MCP', slug: 'contributing/skills/reverse-engineering/7-mcp' },
									],
								},
							],
						},
						{
							label: 'Apps',
							collapsed: true,
							items: [
								{ label: 'Overview', slug: 'contributing/apps/overview' },
							],
						},
						{ label: 'Roadmap & proposals', slug: 'contributing/roadmap-and-proposals' },
					],
				},
				{
					label: 'Research',
					collapsed: true,
					items: [
						{ label: 'Overview', slug: 'research/overview' },
						{ label: 'Ontology', autogenerate: { directory: 'research/ontology' }, collapsed: true },
						{ label: 'Platforms', autogenerate: { directory: 'research/platforms' }, collapsed: true },
						{ label: 'Identity & spaces', autogenerate: { directory: 'research/identity-and-spaces' }, collapsed: true },
						{ label: 'Relationships & events', autogenerate: { directory: 'research/relationships-and-events' }, collapsed: true },
						{ label: 'Context & ecosystem', autogenerate: { directory: 'research/context' }, collapsed: true },
						{ label: 'DX patterns', autogenerate: { directory: 'research/dx-patterns' }, collapsed: true },
					],
				},
				{
					label: 'Reference',
					collapsed: true,
					items: [
						{ label: 'Shapes', autogenerate: { directory: 'reference/shapes' }, collapsed: true },
						{ label: 'Skills', autogenerate: { directory: 'reference/skills' }, collapsed: true },
					],
				},
			],
		}),
	],
});
