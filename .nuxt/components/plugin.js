import Vue from 'vue'
import { wrapFunctional } from './utils'

const components = {
  Footer: () => import('../../components/Footer.vue' /* webpackChunkName: "components/footer" */).then(c => wrapFunctional(c.default || c)),
  Navbar: () => import('../../components/Navbar.vue' /* webpackChunkName: "components/navbar" */).then(c => wrapFunctional(c.default || c)),
  PartnersHowItWork: () => import('../../components/partners/HowItWork.vue' /* webpackChunkName: "components/partners-how-it-work" */).then(c => wrapFunctional(c.default || c)),
  PartnersHowItWorkVar: () => import('../../components/partners/HowItWorkVar.vue' /* webpackChunkName: "components/partners-how-it-work-var" */).then(c => wrapFunctional(c.default || c)),
  StoragesCardEdit: () => import('../../components/storages/CardEdit.vue' /* webpackChunkName: "components/storages-card-edit" */).then(c => wrapFunctional(c.default || c)),
  StoragesCardOrder: () => import('../../components/storages/CardOrder.vue' /* webpackChunkName: "components/storages-card-order" */).then(c => wrapFunctional(c.default || c)),
  StoragesSearchResultItem: () => import('../../components/storages/SearchResultItem.vue' /* webpackChunkName: "components/storages-search-result-item" */).then(c => wrapFunctional(c.default || c)),
  SharedAccount: () => import('../../components/shared/Account.vue' /* webpackChunkName: "components/shared-account" */).then(c => wrapFunctional(c.default || c)),
  SharedAddingFile: () => import('../../components/shared/AddingFile.vue' /* webpackChunkName: "components/shared-adding-file" */).then(c => wrapFunctional(c.default || c)),
  SharedCheckbox: () => import('../../components/shared/Checkbox.vue' /* webpackChunkName: "components/shared-checkbox" */).then(c => wrapFunctional(c.default || c)),
  SharedCoreArea: () => import('../../components/shared/CoreArea.vue' /* webpackChunkName: "components/shared-core-area" */).then(c => wrapFunctional(c.default || c)),
  SharedCoreButton: () => import('../../components/shared/CoreButton.vue' /* webpackChunkName: "components/shared-core-button" */).then(c => wrapFunctional(c.default || c)),
  SharedCoreCheckbox: () => import('../../components/shared/CoreCheckbox.vue' /* webpackChunkName: "components/shared-core-checkbox" */).then(c => wrapFunctional(c.default || c)),
  SharedCoreInput: () => import('../../components/shared/CoreInput.vue' /* webpackChunkName: "components/shared-core-input" */).then(c => wrapFunctional(c.default || c)),
  SharedDefaultArea: () => import('../../components/shared/DefaultArea.vue' /* webpackChunkName: "components/shared-default-area" */).then(c => wrapFunctional(c.default || c)),
  SharedDefaultButton: () => import('../../components/shared/DefaultButton.vue' /* webpackChunkName: "components/shared-default-button" */).then(c => wrapFunctional(c.default || c)),
  SharedDefaultInput: () => import('../../components/shared/DefaultInput.vue' /* webpackChunkName: "components/shared-default-input" */).then(c => wrapFunctional(c.default || c)),
  SharedDropDownFilter: () => import('../../components/shared/DropDownFilter.vue' /* webpackChunkName: "components/shared-drop-down-filter" */).then(c => wrapFunctional(c.default || c)),
  SharedIcoTitle: () => import('../../components/shared/IcoTitle.vue' /* webpackChunkName: "components/shared-ico-title" */).then(c => wrapFunctional(c.default || c)),
  SharedModal: () => import('../../components/shared/Modal.vue' /* webpackChunkName: "components/shared-modal" */).then(c => wrapFunctional(c.default || c)),
  SharedSelecter: () => import('../../components/shared/Selecter.vue' /* webpackChunkName: "components/shared-selecter" */).then(c => wrapFunctional(c.default || c)),
  SharedTag: () => import('../../components/shared/Tag.vue' /* webpackChunkName: "components/shared-tag" */).then(c => wrapFunctional(c.default || c)),
  SharedTitleBig: () => import('../../components/shared/TitleBig.vue' /* webpackChunkName: "components/shared-title-big" */).then(c => wrapFunctional(c.default || c)),
  SharedTitleMedium: () => import('../../components/shared/TitleMedium.vue' /* webpackChunkName: "components/shared-title-medium" */).then(c => wrapFunctional(c.default || c)),
  SharedTitleSmall: () => import('../../components/shared/TitleSmall.vue' /* webpackChunkName: "components/shared-title-small" */).then(c => wrapFunctional(c.default || c)),
  SharedTypeStorageFilter: () => import('../../components/shared/TypeStorageFilter.vue' /* webpackChunkName: "components/shared-type-storage-filter" */).then(c => wrapFunctional(c.default || c)),
  SharedSectionlanding2: () => import('../../components/shared/sectionlanding2.vue' /* webpackChunkName: "components/shared-sectionlanding2" */).then(c => wrapFunctional(c.default || c)),
  SharedPicker: () => import('../../components/shared/picker/index.js' /* webpackChunkName: "components/shared-picker" */).then(c => wrapFunctional(c.default || c)),
  SharedPickerWrapper: () => import('../../components/shared/picker/wrapper.js' /* webpackChunkName: "components/shared-picker-wrapper" */).then(c => wrapFunctional(c.default || c)),
  SharedPickerComponentsVuePicker: () => import('../../components/shared/picker/components/VuePicker.vue' /* webpackChunkName: "components/shared-picker-components-vue-picker" */).then(c => wrapFunctional(c.default || c)),
  SharedPickerComponentsVuePickerOption: () => import('../../components/shared/picker/components/VuePickerOption.vue' /* webpackChunkName: "components/shared-picker-components-vue-picker-option" */).then(c => wrapFunctional(c.default || c)),
  SharedPickerMixinsAttrs: () => import('../../components/shared/picker/mixins/attrs.js' /* webpackChunkName: "components/shared-picker-mixins-attrs" */).then(c => wrapFunctional(c.default || c)),
  SharedPickerMixinsDropdownControls: () => import('../../components/shared/picker/mixins/dropdown-controls.js' /* webpackChunkName: "components/shared-picker-mixins-dropdown-controls" */).then(c => wrapFunctional(c.default || c)),
  SharedPickerMixinsKeyControls: () => import('../../components/shared/picker/mixins/key-controls.js' /* webpackChunkName: "components/shared-picker-mixins-key-controls" */).then(c => wrapFunctional(c.default || c)),
  SharedPickerHelpersOuterClick: () => import('../../components/shared/picker/helpers/outer-click.js' /* webpackChunkName: "components/shared-picker-helpers-outer-click" */).then(c => wrapFunctional(c.default || c))
}

for (const name in components) {
  Vue.component(name, components[name])
  Vue.component('Lazy' + name, components[name])
}
