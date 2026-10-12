const RequiredRolesComponent = {
  render() {
    const restrictedRoles = Array.isArray(this.$attrs['x-roles-required'])
      ? this.$attrs['x-roles-required']
      : []
    const scopedRoles = Array.isArray(this.$attrs['x-roles-scoped'])
      ? this.$attrs['x-roles-scoped']
      : []
    if (restrictedRoles.length === 0 && scopedRoles.length === 0) return null

    const vueComponents = []

    if (restrictedRoles.length !== 0) {
      vueComponents.push(
        Vue.h('div', { class: 'text-sm' }, [
          Vue.h(
            'div',
            { style: { marginBottom: '4px' } },
            'This action is restricted to the following role' +
              (restrictedRoles.length > 1 ? 's' : '') +
              ':',
          ),
          Vue.h(
            'ul',
            { class: 'mb-0 list-none p-0' },
            restrictedRoles.map((role) =>
              Vue.h(
                'li',
                { class: 'font-code text-c-2', style: { fontWeight: 600 } },
                role,
              ),
            ),
          ),
        ]),
      )
    }

    if (scopedRoles.length !== 0) {
      vueComponents.push(
        Vue.h('div', { class: 'text-sm' }, [
          Vue.h(
            'div',
            { style: { marginBottom: '4px' } },
            'This action has additional content available to a token resource owner or an application with one of these role' +
              (scopedRoles.length > 1 ? 's' : '') +
              ':',
          ),
          Vue.h(
            'ul',
            { class: 'mb-0 list-none p-0' },
            scopedRoles.map((role) =>
              Vue.h(
                'li',
                { class: 'font-code text-c-2', style: { fontWeight: 600 } },
                role,
              ),
            ),
          ),
        ]),
      )
    }

    return Vue.h('div', { class: 'mt-6' }, [
      Vue.h(
        'div',
        { class: 'text-c-1 mt-3 mb-3 text-lg leading-[1.45] font-medium' },
        'Required Roles',
      ),
      Vue.h(
        'div',
        {
          style: {
            display: 'flex',
            alignItems: 'flex-start',
            gap: '8px',
            border: '1px solid #f59e0b',
            background: 'rgba(245, 158, 11, 0.1)',
            borderRadius: '6px',
            padding: '10px 12px',
          },
        },
        [
          Vue.h('span', { style: { fontSize: '16px', lineHeight: '1.2' } }, '⚠️'),
          Vue.h('div', {}, vueComponents),
        ],
      ),
    ])
  },
}

export default function requiredRolesPlugin() {
  return {
    name: 'required-roles-plugin',
    extensions: [
      { name: 'x-roles-required', component: RequiredRolesComponent },
      { name: 'x-roles-scoped', component: RequiredRolesComponent },
    ],
  }
}